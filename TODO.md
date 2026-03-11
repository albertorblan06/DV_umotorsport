# HIGH PRIORITY (Firmware & Core Perception)

- [ ] **PID tuning** - tune kp/ki/kd now that steering gears are fixed and outputLimit works
- [ ] **Verify outputLimit clamp** - send a target beyond limit, confirm it clamps correctly
- [ ] **Export YOLOv11n nano model to TensorRT FP16 for ~10ms inference**
- [ ] **New YOLOv11 nano model training** (y540, 300 epochs)

---

# MEDIUM PRIORITY (Optimization & Infrastructure)

- [ ] **Benchmark YOLOv10n vs v11n on Orin with TensorRT**
- [ ] **Crop sky from camera input** - crop top N% before inference, or use rectangular input (e.g. `imgsz=(384,640)`)
- [ ] **Investigate zombie process accumulation on Orin**

---

# LOW PRIORITY (Documentation & Long-Term)

- [ ] **Create reproducible Orin setup script/guide**
- [ ] **Full autonomous loop:** camera -> detection -> planning -> actuation
- [ ] **Trajectory planning from cone positions**
- [ ] **Make a map of the university**

---

# COMPLETED

- [x] **Fix kart oversteering with YOLO pipeline** (DONE 2026-03-11) - steering_gain halved to 0.5, exposed as `steering_gain` launch arg in autonomous.launch.py. Diagnostic test in tests/test_steering_gain.py.
- [x] **Remove raw value display from dashboard skins** (DONE 2026-03-11) - All four skins (Default, KITT, Tesla, HUD) updated to show calibrated degrees only.
- [x] **Include manual remote control of the kart via the dashboard** (DONE 2026-03-11)
  - [x] Add joystick input functionality when "manual" button is clicked
  - [x] Add switch to choose PWM or angle target for steering
  - [x] Map another axis to desired acceleration/braking (UI only for now)
- [x] **Investigate rviz window accumulation on Orin** (DONE 2026-03-11) - Added cleanup logic to run_live.sh, display_zed_cam.launch.py, autonomous.launch.py, and gui.launch.py. Diagnostic test in tests/test_rviz_accumulation.py.
