# Investigation: rviz Window Accumulation on Orin

**Date:** 2026-03-11
**Status:** Investigation complete, fix pending deployment
**Related TODO:** "Investigate rviz window accumulation on Orin -- launch file opens multiple rviz instances, causes freezes"

---

## Summary of Findings

After a thorough analysis of all 9 launch files in `kart_brain/src/` and both shell runner scripts (`run_live.sh`, `run_live_3d.sh`), the root cause is **not a single launch file spawning multiple rviz instances**. Instead, the accumulation is caused by a combination of factors:

1. **No stale process cleanup in most launch paths.**
2. **GUI viewer processes (`rqt_image_view`) launched without guards.**
3. **The `display_zed_cam.launch.py` ThirdParty file spawns rviz2 directly**, and can be included or run manually alongside other launches that already provide visualization.

---

## Launch File Inventory

### Files that spawn GUI/visualization nodes:

| Launch File | GUI Nodes Spawned | Cleanup Logic |
|---|---|---|
| `kart_bringup/autonomous.launch.py` | `steering_hud` (OpenCV window) | None |
| `kart_bringup/gui.launch.py` | `hud_viewer` (OpenCV window) | None |
| `kart_bringup/dashboard.launch.py` | None (web only) | None |
| `kart_bringup/teleop.launch.py` | None | None |
| `kart_perception/perception_3d.launch.py` | `cone_marker_viz_3d` (publishes RViz markers) | None |
| `kart_perception/perception_test.launch.py` | `cone_marker_viz` (publishes RViz markers) | None |
| `kart_sim/simulation.launch.py` | `cone_marker_viz_3d`, `dashboard` | None |
| `ThirdParty/zed_display_rviz2/display_zed_cam.launch.py` | **rviz2** (direct Node) + ZED wrapper | None |
| `run_live.sh` (shell) | `rqt_image_view` (backgrounded `&`) | None |
| `run_live_3d.sh` (shell) | `rqt_image_view` (backgrounded `&`) | **Yes** (killall + pkill at start) |

### Files that include other launch files (nesting):

| Parent Launch | Includes | Risk |
|---|---|---|
| `kart_bringup/autonomous.launch.py` | `perception_3d.launch.py` | `perception_3d` spawns `cone_marker_viz_3d` which publishes RViz markers. If a user manually opens rviz2 to view these markers, and then also runs `display_zed_cam.launch.py`, two rviz windows exist. |
| `kart_sim/simulation.launch.py` | `perception_3d.launch.py` (conditional, use_yolo=true) | Same marker publishing risk. |
| `ThirdParty/display_zed_cam.launch.py` | `zed_camera.launch.py` | If autonomous.launch.py is already running (which also includes `zed_camera`), the ZED wrapper launches twice AND rviz2 is added on top. |

---

## Root Cause Analysis

The rviz accumulation happens through this sequence on the Orin:

1. User launches `autonomous.launch.py` (or `run_live_3d.sh`). This starts the full pipeline including `steering_hud` (an OpenCV-based HUD window) and `cone_marker_viz_3d` (which publishes MarkerArray to `/perception/cones_3d_markers`).

2. To visualize the 3D cone markers, the user (or a script) runs `display_zed_cam.launch.py` which spawns an **rviz2 node**. This is the only launch file that directly instantiates rviz2.

3. If the user Ctrl+C's the autonomous pipeline and relaunches it, the **rviz2 process from step 2 is not killed** because it was launched from a separate terminal/command. The new launch creates a new set of marker publishers, and the old rviz2 might still be running.

4. If the user runs `display_zed_cam.launch.py` again (to get rviz2 back), a **second rviz2 instance** is spawned. Repeat N times = N rviz2 windows.

5. On the Orin (limited GPU memory), each rviz2 instance consumes significant GPU/CPU resources. After 3-4 instances, the system freezes.

**Key evidence from error_log.md:** Entry `2026-02-22 - Duplicate YOLO detector processes consuming all GPU` documents the exact same pattern but with YOLO processes. The `run_live_3d.sh` script was updated with cleanup logic (`killall`, `pkill`) to prevent that specific case, but no equivalent cleanup was added for rviz2 or `rqt_image_view` in the launch files.

---

## Additional Risk: `rqt_image_view` in shell scripts

Both `run_live.sh` and `run_live_3d.sh` launch `rqt_image_view` as a **backgrounded process** (`&`). Only `run_live_3d.sh` has cleanup logic at the top. If `run_live.sh` is run multiple times, `rqt_image_view` processes accumulate.

---

## Proposed Fix

### 1. Add cleanup to `autonomous.launch.py` (pre-launch event)
Add an `ExecuteProcess` action at the start of the launch that kills stale rviz2 and rqt_image_view processes:
```python
cleanup = ExecuteProcess(
    cmd=["bash", "-c", 
         "killall -q rviz2 rqt_image_view 2>/dev/null; sleep 0.5"],
    output="log",
)
```

### 2. Add cleanup to `run_live.sh`
Mirror the cleanup logic already present in `run_live_3d.sh`:
```bash
killall -q rqt_image_view rviz2 2>/dev/null
pkill -f "rqt_image_view|rviz2" 2>/dev/null
sleep 1
```

### 3. Add singleton guard to `display_zed_cam.launch.py`
Before spawning rviz2, check if one is already running. If so, skip launching a new instance:
```python
check_rviz = ExecuteProcess(
    cmd=["bash", "-c", "pgrep -x rviz2 && echo 'rviz2 already running, skipping' || exit 1"],
    ...
)
```

### 4. Create a unified `gui.launch.py` that is the single entry point for all visualization
Instead of having users manually run `display_zed_cam.launch.py`, consolidate rviz2 launching into `kart_bringup/gui.launch.py` with proper cleanup.

---

## Files to Modify

| File | Change |
|---|---|
| `kart_bringup/launch/autonomous.launch.py` | Add cleanup action at start |
| `run_live.sh` | Add stale process cleanup |
| `kart_bringup/launch/gui.launch.py` | Add rviz2 node with cleanup and singleton guard |

---

## Diagnostic Test Plan

A Python script (`tests/test_rviz_accumulation.py`) will:
1. Parse all `.launch.py` files and extract Node declarations.
2. Flag any `rviz2` or `rqt_image_view` Node that lacks a corresponding cleanup action in the same launch description.
3. Check shell scripts for backgrounded GUI processes without matching cleanup.
4. Report violations as test failures.

This ensures any future launch file changes that introduce GUI nodes without cleanup are caught automatically.