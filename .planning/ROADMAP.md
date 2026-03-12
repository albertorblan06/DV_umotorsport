# Roadmap: DV_umotorsport

## Phase 1: Subsystem Stabilization & Integration Testing
**Goal:** Ensure perception, actuation, and communication systems are robust and reliable independently and in simulation before full autonomy. The immediate focus is a comprehensive and methodical reorganization of all project documentation into clean markdown format.

**Plans:** 2 plans
- [ ] 01-01-PLAN.md — Foundation & Software Documentation
- [ ] 01-02-PLAN.md — Hardware Documentation

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
**Goal:** Create a comprehensive, from-scratch documentation suite for the Full Autonomous Navigation architecture. Per user decisions, this phase structurally addresses the requirements by establishing the complete architectural blueprints and system designs for the autonomous software and hardware.

**Plans:** 2 plans
- [ ] 02-01-PLAN.md — Foundation & Hardware Docs
- [ ] 02-02-PLAN.md — Software Docs & LLM Aggregation

**Requirements:**
- AUTO-01: Kart can autonomously navigate a track defined by traffic cones. (Structurally addressed via architectural documentation)
- AUTO-03: System detects when the track is completed. (Structurally addressed via integration documentation)

**Success Criteria:**
1. A new `docs/` folder exists with hardware, assembly, software, and integration subfolders.
2. `scripts/generate_llms_txt.py` successfully aggregates all markdown files into `llms.txt`.
3. The documentation provides a complete architectural blueprint for AUTO-01 and AUTO-03 without using emojis.
