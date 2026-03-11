# Immediate Tasks

## ESP32 Firmware
- [ ] **PID tuning** -- tune kp/ki/kd now that steering gears are fixed and outputLimit works
- [ ] **Verify outputLimit clamp** -- send a target beyond limit, confirm it clamps correctly

## Perception Optimization
- [ ] **Export YOLOv11n nano model to TensorRT FP16 for ~10ms inference**
- [ ] New YOLOv11 nano model training (y540, 300 epochs)
- [ ] **Benchmark YOLOv10n vs v11n on Orin with TensorRT**
- [ ] **Crop sky from camera input** -- crop top N% before inference, or use rectangular input (e.g. `imgsz=(384,640)`)

## Infrastructure
- [ ] Investigate zombie process accumulation on Orin
- [ ] Create reproducible Orin setup script/guide

## Long-Term
- [ ] Full autonomous loop: camera -> detection -> planning -> actuation
- [ ] Trajectory planning from cone positions
- [ ] Make a map of the university

---

# Completed

- [x] **Investigate rviz window accumulation on Orin** (Iteration 1, 2026-03-11)
- [x] **Include manual remote control of the kart via the dashboard** (Iteration 2, 2026-03-11)
  - [x] Add joystick input functionality when "manual" button is clicked
  - [x] Add switch to choose PWM or angle target for steering
  - [x] Map another axis to desired acceleration/braking (UI only for now)
- [x] **Fix kart oversteering with YOLO pipeline** (Iteration 3, 2026-03-11) -- steering_gain halved to 0.5, exposed as launch arg
- [x] **Remove raw value display from dashboard skins** (Iteration 3, 2026-03-11) -- all four skins updated
