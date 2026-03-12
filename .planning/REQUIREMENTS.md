# Requirements: DV_umotorsport

**Defined:** 2026-03-12
**Core Value:** Reliable, real-time autonomous control of a racing kart utilizing a unified computer vision pipeline and robust low-level actuator management.

## v1 Requirements

### Core Autonomy
- [x] **AUTO-01**: Kart can autonomously navigate a track defined by traffic cones.
- [x] **AUTO-02**: Planner generates feasible racing lines based on localized cones.
- [ ] **AUTO-03**: System detects when the track is completed.

### Perception
- [ ] **PERC-01**: Detects track boundaries/cones at >= 15Hz using YOLOv11 and ZED.
- [ ] **PERC-02**: Converts bounding boxes and depth to 3D local coordinates.

### Control & Actuation
- [ ] **CTRL-01**: ESP32 outputs PWM to steering with accurate AS5600 feedback.
- [ ] **CTRL-02**: ESP32 drives Throttle and Brake DACs reliably.
- [ ] **CTRL-03**: ESP32 heartbeat failure leads to safe state (brakes applied).

### Telemetry
- [x] **TELE-01**: ROS 2 dashboard displays current state, speeds, and camera feeds.

## v2 Requirements

### Advanced Planning
- **PLAN-01**: Dynamic obstacle avoidance during racing.
- **PLAN-02**: Model Predictive Control (MPC) for high-speed trajectory tracking.

## Out of Scope

| Feature | Reason |
|---------|--------|
| Cellular Teleop | Not required for local track autonomy. |
| Non-cone tracks | Project is scoped to formula student-style cone tracks. |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| AUTO-01 | Phase 2 | Complete |
| AUTO-02 | Phase 1 | Complete |
| AUTO-03 | Phase 2 | Pending |
| PERC-01 | Phase 1 | Pending |
| PERC-02 | Phase 1 | Pending |
| CTRL-01 | Phase 1 | Pending |
| CTRL-02 | Phase 1 | Pending |
| CTRL-03 | Phase 1 | Pending |
| TELE-01 | Phase 1 | Complete |

**Coverage:**
- v1 requirements: 9 total
- Mapped to phases: 9
- Unmapped: 0 ✓

---
*Requirements defined: 2026-03-12*
*Last updated: 2026-03-12 after initial definition*