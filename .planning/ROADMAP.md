# Roadmap: DV_umotorsport

## Phase 1: Subsystem Stabilization & Integration Testing
**Goal:** Ensure perception, actuation, and communication systems are robust and reliable independently and in simulation before full autonomy.

**Requirements:**
- AUTO-02: Planner generates feasible racing lines based on localized cones.
- PERC-01: Detects track boundaries/cones at >= 15Hz using YOLOv11 and ZED.
- PERC-02: Converts bounding boxes and depth to 3D local coordinates.
- CTRL-01: ESP32 outputs PWM to steering with accurate AS5600 feedback.
- CTRL-02: ESP32 drives Throttle and Brake DACs reliably.
- CTRL-03: ESP32 heartbeat failure leads to safe state (brakes applied).
- TELE-01: ROS 2 dashboard displays current state, speeds, and camera feeds.

**Success Criteria:**
1. Orin can successfully detect cones and generate local map at 15+ Hz.
2. ESP32 accurately tracks steering setpoints and drives throttle/brake.
3. Disconnecting serial triggers safe state within 1 second.
4. Dashboard connects and streams valid telemetry.

## Phase 2: Full Autonomous Navigation
**Goal:** Achieve end-to-end autonomous navigation around physical cone tracks.

**Requirements:**
- AUTO-01: Kart can autonomously navigate a track defined by traffic cones.
- AUTO-03: System detects when the track is completed.

**Success Criteria:**
1. Kart completes a lap of an autocross track without hitting cones.
2. The planner smoothly handles sharp hairpins without losing the track.
3. The system gracefully stops upon detecting lap completion or track loss.
