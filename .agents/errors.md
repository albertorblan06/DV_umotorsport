# Errors and Lessons Learned

Every agent session must record failed assumptions, errors, or bugs in this file. Before starting a new session, review this document to avoid repeating past mistakes.

## Format

```
## YYYY-MM-DD - Brief title
**Context:** What was being attempted
**What happened:** What went wrong (stack trace, command, bug)
**Resolution/Lesson:** How it was fixed and the prevention rule
```

---

## Error Log

## 2026-03-11 - Cloned kart_docs into wrong directory
**Context:** Setting up the initial repository structure.
**What happened:** Cloned the `kart_docs` repository directly into the root folder instead of inside its own subdirectory, mixing files.
**Resolution/Lesson:** Moved all `kart_docs` files into a dedicated subdirectory. Rule: Always verify the target directory path when running `git clone` or creating files. The three subsystems (`kart_brain`, `kart_medulla`, `kart_docs`) must stay in their respective folders under the root.

## 2026-03-11 - Claimed ESP32 uses custom binary protocol when it already uses nanopb/protobuf
**Context:** User asked about protobuf in the project.
**What happened:** Found `proto/kart_msgs.proto` but relied on stale memory info ("custom binary protocol over UART") instead of checking the actual codebase. Commit `3a9999e` had already migrated both sides. Missed `proto/generated_c/` and `proto/nanopb/` directories.
**Resolution/Lesson:** Rule: When answering questions about what the codebase uses, CHECK THE CODE -- not memory. If you find a .proto file, check for generated code too (`generated_c/`, `*_pb2.py`, `nanopb/`).

## 2026-03-09 - Tried SSH to wrong host (orin) instead of reading user's message
**Context:** User said their bot is on "ssh debian".
**What happened:** Ran `ssh orin` (which timed out) instead of `ssh debian`, then asked unnecessary questions about hostname/credentials.
**Resolution/Lesson:** Rule: Read the user's message carefully before acting. If they say "ssh debian", use `ssh debian`. Do not substitute a different host. Do not ask questions you can answer by trying.

## 2026-03-09 - Reported training "in progress" when process had already crashed
**Context:** User asked for training status on y540-ubuntu.
**What happened:** Grepped the log, saw no completed epoch lines, and reported "still on epoch 0." Did NOT check whether the process was actually running (`ps aux`) or GPU was active (`nvidia-smi`). The training had crashed with `CUDNN_STATUS_INTERNAL_ERROR`.
**Resolution/Lesson:** Rule: When checking remote training status, ALWAYS check BOTH the log AND the process. Run `nvidia-smi` + `ps aux | grep python` alongside any log grep. A status check is: (1) is the process alive? (2) is the GPU active? (3) what does the log say? -- in that order.

## 2026-03-07 - ZED "CAMERA NOT DETECTED" after reboot
**Context:** After rebooting the Orin, the ZED SDK reported `CAMERA NOT DETECTED` even though `lsusb` showed the device.
**What happened:** The USB controller does not fully re-enumerate the ZED after a warm reboot. The device appears in `lsusb` but the SDK cannot claim the interface.
**Resolution/Lesson:** Software USB reset: `echo "0" | sudo -S bash -c "echo 0 > /sys/bus/usb/devices/2-3.2/authorized && sleep 1 && echo 1 > /sys/bus/usb/devices/2-3.2/authorized"`. Rule: Always do a software USB reset before launching ZED nodes.

## 2026-03-07 - Claimed dashboard fix was working without visual verification
**Context:** Made multiple changes to the dashboard (raw steering value, WebSocket port, QoS fix).
**What happened:** Repeatedly claimed changes were "verified" based on source files and grep output, but the dashboard showed all zeros in the browser. Root causes: old process still running, stale .pyc cache, wrong WebSocket port, different server.py variant on Orin.
**Resolution/Lesson:** Rule: A dashboard change is NOT verified until the browser shows correct values. Before restarting a node, kill old processes (`ss -tlnp | grep <port>`). After Python changes with symlink-install, delete `__pycache__` dirs AND restart the node. Check which server.py variant is deployed.

## 2026-03-07 - Acted without user confirmation, misread instructions
**Context:** Multiple instances of acting on assumptions instead of reading user's actual words.
**What happened:** User asked "ok turn off orin?" (a question) -- ran `shutdown now` without permission. User said "kill yourself" (kill the process) -- tried to relaunch instead. User said "note this as serious error and commit" -- also tried to fix and relaunch.
**Resolution/Lesson:** Rule: Read the user's message literally before acting. A question mark means they are asking, not instructing. Do exactly what was asked, nothing more. Never run destructive/irreversible commands (shutdown, delete, force-push) without explicit confirmation.

## 2026-03-07 - Dashboard port 8080 "address already in use"
**Context:** Every dashboard relaunch crashes with `OSError: address already in use`.
**What happened:** Server does not set `SO_REUSEADDR`. Background `nohup` processes survive terminal sessions and hold the port.
**Resolution/Lesson:** Set `SO_REUSEADDR` on the server socket. Before launching dashboard, always run `fuser -k 8080/tcp`. Avoid `nohup` for dashboard. Rule: Always check `ss -tlnp | grep 8080` before relaunching.

## 2026-03-03 - Tried to flash ESP32 from Mac instead of Orin
**Context:** Asked to flash the ESP32 and update code on the Orin.
**What happened:** Checked for USB devices on the local Mac instead of SSHing to the Orin.
**Resolution/Lesson:** Rule: ALL hardware (ESP32, cameras, actuators) is on the Orin. The Mac is only for development. For any hardware interaction, always SSH to the Orin first.

## 2026-02-28 - Failed to visually validate trajectory -- kart exited track undetected
**Context:** After training a neural_v2 controller with cone-proximity penalty.
**What happened:** Generated a trajectory plot and claimed "0 boundary violations" and "trajectory stays between cones." The trajectory went far outside cone boundaries (y=30, cones only to y=23). Root cause: centerline was hardcoded, and "validation" only checked distance to individual cone points, not boundary line segments. Actual analysis: 1324/2001 steps outside track.
**Resolution/Lesson:** Rule: Always visually inspect generated plots with critical eyes. Track boundaries are line segments between consecutive cones, not just points -- use polygon-based boundary checking.

## 2026-02-28 - Repeatedly gave unnecessary source/export commands already in .bashrc
**Context:** Giving launch instructions for Gazebo simulation.
**What happened:** Kept including `source /opt/ros/humble/setup.bash` etc., despite these being in `.bashrc`. Repeated even after documenting the error.
**Resolution/Lesson:** Rule: All environment setup is in `.bashrc` on every machine. Just run commands directly -- never prepend source/export boilerplate.

## 2026-02-28 - Wrote to wrong file instead of asking where it goes
**Context:** User asked to add a FAQ entry to "kart_docs".
**What happened:** Assumed the file did not exist and wrote to `.agents/README.md` in `kart_brain` instead of `kart_docs/docs/faq.md`.
**Resolution/Lesson:** Rule: If the user references a file or location you do not recognize, ASK. Do not assume and write to a different location.

## 2026-02-28 - Created files but didn't rebuild workspace before telling user to launch
**Context:** Created `hairpin_track.sdf` and updated `simulation.launch.py` on the Mac.
**What happened:** Told the user the launch commands without rebuilding the workspace. The `install(DIRECTORY worlds/ ...)` in CMakeLists only copies files at build time.
**Resolution/Lesson:** Rule: After creating or modifying any file under `src/`, scp to the target and rebuild. Development happens on Mac, Gazebo runs on VM. Always source ROS explicitly in SSH commands (`.bashrc` is NOT sourced in non-interactive SSH).

## 2026-02-25 - cuBLAS fails on Jetson: pip cuBLAS 12.9 vs system CUDA 12.6
**Context:** Running `torch.matmul` on the Orin.
**What happened:** `CUBLAS_STATUS_ALLOC_FAILED when calling cublasCreate(handle)`. pip installed `nvidia-cublas-cu12==12.9.1.4`, incompatible with the Jetson's system CUDA 12.6. Pip libs loaded first in `LD_LIBRARY_PATH`.
**Resolution/Lesson:** In launch scripts, prepend `/usr/local/cuda-12.6/targets/aarch64-linux/lib` to `LD_LIBRARY_PATH` before pip NVIDIA libs. Rule: On Jetson, system CUDA libs must always precede pip-installed NVIDIA libs.

## 2026-02-25 - YOLOv5 torch.hub broken with torch 2.10
**Context:** Using `torch.hub.load("ultralytics/yolov5", "custom", ...)`.
**What happened:** YOLOv5 source from GitHub is incompatible with torch 2.10 -- passes raw numpy arrays to `conv2d()` instead of tensors.
**Resolution/Lesson:** Migrated to `ultralytics` pip package API. Switched to YOLOv11 weights. Rule: Prefer the `ultralytics` pip package over `torch.hub.load`.

## 2026-02-24 - Multiple failed torch install attempts on Jetson Orin
**Context:** Original JetPack PyTorch overwritten during dependency installation.
**What happened:** Four recovery attempts failed with various incompatibilities between PyPI torch, NVIDIA wheels, torchvision, and CUDA.
**Resolution/Lesson:** Rule: Never `pip install torch` without `--extra-index-url` pointing to the Jetson wheel index. Always verify CUDA immediately after install. Pin `numpy<2`. Never install torchvision from PyPI on Jetson.

## 2026-02-22 - BGR/RGB swap in YOLO annotated image
**Context:** Live camera feed in rqt_image_view showed inverted colors.
**What happened:** `image_source_node` publishes BGR, `yolo_detector_node` converts to RGB for inference, then publishes with `encoding="bgr8"` without converting back.
**Resolution/Lesson:** Added `cv2.cvtColor(rendered[0], cv2.COLOR_RGB2BGR)` before publishing. Rule: OpenCV uses BGR, ROS Image with "bgr8" expects BGR, YOLO/PIL work in RGB. Always verify channel order matches declared encoding.

## 2026-02-22 - Duplicate YOLO detector processes consuming all GPU
**Context:** Multiple `yolo_detector` instances running from both script and manual launches.
**What happened:** Each consumed ~500-800% CPU and GPU memory. System sluggish.
**Resolution/Lesson:** Rule: Before launching nodes, check for existing instances: `ps aux | grep yolo_detector`. Kill stale processes before launching new ones.

## 2026-02-22 - Wrong IP for y540 laptop
**Context:** Connecting to y540 laptop over SSH.
**What happened:** Laptop had DHCP IP 10.7.20.138 but was given as 10.7.20.136. Multiple failed connection attempts.
**Resolution/Lesson:** Rule: All machines on Robots_urjc use DHCP -- IPs can change. Always verify with `hostname -I`. Always label IPs with machine name. SSH config hostnames are source of truth.

## 2026-02-22 - SSH server not installed on fresh Ubuntu laptop
**Context:** Trying to SSH into y540.
**What happened:** "Connection refused" -- openssh-server not installed.
**Resolution/Lesson:** Rule: First step for remote access on a new machine is always `sudo apt install -y openssh-server` physically.

## 2026-02-22 - ZED SDK installer breaks pip permissions
**Context:** Installing ZED SDK on Orin.
**What happened:** Installer runs pip as root, leaving `.dist-info` dirs owned by root with no world-read permission. Subsequent pip install fails with PermissionError.
**Resolution/Lesson:** After ZED SDK install: `sudo chmod -R a+rX /usr/local/lib/python3.10/dist-packages/`. Rule: When any installer runs pip as root, check permissions afterward.

## 2026-02-22 - PyTorch installed as CPU-only (Jetson AI Lab index unreachable)
**Context:** Installing PyTorch on Orin.
**What happened:** The Jetson AI Lab index DNS failed. Pip silently fell back to PyPI and installed CPU-only torch. Also pulled numpy 2.x, breaking pyzed and cv2.
**Resolution/Lesson:** Rule: After installing PyTorch, always verify CUDA: `python3 -c "import torch; print(torch.version.cuda, torch.cuda.is_available())"`. Pin numpy after any torch install. Verify the extra-index-url is reachable first.

## 2026-02-22 - AnyDesk black screen without ConnectedMonitor Xorg option
**Context:** Using AnyDesk on Orin.
**What happened:** NVIDIA driver saw DFP-0 and DFP-1 as "disconnected" (dummy plug via DP-to-HDMI adapter lacks proper EDID). Xorg had no screen.
**Resolution/Lesson:** Created `/etc/X11/xorg.conf.d/10-virtual-display.conf` with `Option "ConnectedMonitor" "DFP-0"` to force framebuffer on DisplayPort.

## 2026-02-21 - Cone geometry invisible in Gazebo Fortress
**Context:** Used `<cone>` SDF geometry for track cones.
**What happened:** Gazebo Fortress (SDF 1.6) does not support cone geometry -- silently renders nothing and logs `Geometry type [0] not supported`.
**Resolution/Lesson:** Replaced all `<cone>` with `<cylinder>`. Rule: Only use geometries supported by Fortress: box, sphere, cylinder, capsule, ellipsoid, plane, mesh.

## 2026-02-21 - Odometry at (0,0) despite kart spawned at (20,0)
**Context:** `perfect_perception_node.py` used raw odometry as world position.
**What happened:** Gazebo odometry is relative to spawn pose -- reports (0,0) at startup regardless of world placement. All cones appeared >20m away.
**Resolution/Lesson:** Added spawn position parameters to transform odom into world frame. These MUST match `<pose>` in the SDF file.

## 2026-02-21 - Kart drifts 1000+ meters during Gazebo startup
**Context:** Running with `real_time_factor: 0` (unlimited speed).
**What happened:** Gazebo simulated thousands of seconds during startup. Tiny physics artifacts accumulated into massive odometry drift.
**Resolution/Lesson:** Changed to `real_time_factor: 1`. Rule: Never use `real_time_factor: 0` unless all control nodes are already running.

## 2026-02-21 - Steering joints log velocity control warnings
**Context:** Gazebo logging `Velocity control does not respect positional limits`.
**What happened:** Steering joints had position limits but no effort limits.
**Resolution/Lesson:** Added `<effort>1e6</effort>` to both steering joint limits.

## 2026-02-21 - Wheels start below ground plane
**Context:** Kart model at z=0.15 with wheel radius 0.15.
**What happened:** Wheel bottoms at z=-0.05, embedded in ground. Physics jitter.
**Resolution/Lesson:** Increased model z-offset to 0.22. Rule: Verify `model_z - wheel_z_offset - wheel_radius > 0`.

## 2026-02-21 - sudo requires password over non-interactive SSH
**Context:** Running `ssh utm "sudo apt install ..."`.
**What happened:** sudo needs a TTY for password input. `-t` flag does not help from non-interactive contexts.
**Resolution/Lesson:** Use `ssh <host> 'echo "0" | sudo -S <command>'` for all sudo operations.
