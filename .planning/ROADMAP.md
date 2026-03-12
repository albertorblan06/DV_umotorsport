# Roadmap: DV_umotorsport

## Phases

- [x] **Phase 1: Subsystem Stabilization & Integration Testing** - Ensure perception, actuation, and communication systems are robust and documented.
- [x] **Phase 2: Full Autonomous Navigation** - Comprehensive, from-scratch documentation suite for the Full Autonomous Navigation architecture.
- [ ] **Phase 3: CI/CD & Project Management Foundation** - Establish CI pipelines, code analysis, and tracking boards.
- [ ] **Phase 4: Hardware Abstraction & Logic Decoupling** - Isolate core algorithms from hardware and middleware dependencies.
- [ ] **Phase 5: Unit Testing & Performance Benchmarking** - Implement tests, benchmark latency, and optimize algorithmic complexity.
- [ ] **Phase 6: End-to-End Validation & Regression Testing** - Validate the full system holistically with ROS bags and HIL testing.

## Phase Details

### Phase 1: Subsystem Stabilization & Integration Testing
**Goal:** Ensure perception, actuation, and communication systems are robust and reliable independently and in simulation before full autonomy. The immediate focus is a comprehensive and methodical reorganization of all project documentation into clean markdown format.
**Depends on:** None
**Requirements:** AUTO-02, PERC-01, PERC-02, CTRL-01, CTRL-02, CTRL-03, TELE-01
**Success Criteria:**
1. Orin can successfully detect cones and generate local map at 15+ Hz.
2. ESP32 accurately tracks steering setpoints and drives throttle/brake.
3. Disconnecting serial triggers safe state within 1 second.
4. Dashboard connects and streams valid telemetry.
**Plans:** 01-01, 01-02

### Phase 2: Full Autonomous Navigation
**Goal:** Create a comprehensive, from-scratch documentation suite for the Full Autonomous Navigation architecture. Per user decisions, this phase structurally addresses the requirements by establishing the complete architectural blueprints and system designs for the autonomous software and hardware.
**Depends on:** Phase 1
**Requirements:** AUTO-01, AUTO-03
**Success Criteria:**
1. A new `docs/` folder exists with hardware, assembly, software, and integration subfolders.
2. `scripts/generate_llms_txt.py` successfully aggregates all markdown files into `llms.txt`.
3. The documentation provides a complete architectural blueprint for AUTO-01 and AUTO-03 without using emojis.
**Plans:** 02-01, 02-02

### Phase 3: CI/CD & Project Management Foundation
**Goal:** The development workflow enforces clean code and tracks progress automatically.
**Depends on:** Phase 2
**Requirements:** SCRU-01, METR-01, METR-02
**Success Criteria:**
1. Project board reflects the current sprint and backlog items, tracking development progress.
2. Commits to Pull Requests automatically trigger the CI pipeline.
3. The CI pipeline fails and blocks merging if clang-tidy or Ruff detect code quality violations.
**Plans:** 2 plans
- [ ] 03-01-PLAN.md — Initialize the project tracking foundation via a lightweight GitHub Projects board
- [ ] 03-02-PLAN.md — Establish a rigorous CI pipeline that enforces static analysis rules using Ruff and clang-tidy

### Phase 4: Hardware Abstraction & Logic Decoupling
**Goal:** Core algorithms are isolated from hardware and middleware dependencies.
**Depends on:** Phase 3
**Requirements:** TEST-01, PERF-01
**Success Criteria:**
1. PID and trajectory planning algorithms compile independently without ROS 2 or FreeRTOS headers.
2. Hardware interactions (PWM, UART, ZED SDK) route through virtual C++ interfaces (HAL).
3. The kart's physical behavior remains identical when executing via the newly wrapped HAL interfaces.
**Plans:** TBD

### Phase 5: Unit Testing & Performance Benchmarking
**Goal:** Core algorithms are mathematically optimized and protected by automated tests.
**Depends on:** Phase 4
**Requirements:** TEST-02, TEST-03, PERF-02, PERF-03
**Success Criteria:**
1. CI executes GTest/PyTest for the Orin logic and Unity tests for the ESP32.
2. CI reports algorithmic complexity and execution latency for core functions using Google Benchmark.
3. Trajectory and PID functions consistently execute within the required 10ms (100Hz) latency budget in benchmarks.
**Plans:** TBD

### Phase 6: End-to-End Validation & Regression Testing
**Goal:** The complete system behavior is validated holistically against historical data and physical hardware.
**Depends on:** Phase 5
**Requirements:** METR-03, TEST-04
**Success Criteria:**
1. The computer vision pipeline processes pre-recorded ROS bags and verifies output matches expected spatial localizations.
2. The HIL testbed successfully routes simulated commands to the physical ESP32 and receives accurate telemetry back.
3. Full system regression tests run automatically without needing the physical kart on a track.
**Plans:** TBD

## Progress

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Subsystem Stabilization & Integration Testing | 2/2 | Completed | Yes |
| 2. Full Autonomous Navigation | 2/2 | Completed | Yes |
| 3. CI/CD & Project Management Foundation | 0/0 | Not started | - |
| 4. Hardware Abstraction & Logic Decoupling | 0/0 | Not started | - |
| 5. Unit Testing & Performance Benchmarking | 0/0 | Not started | - |
| 6. End-to-End Validation & Regression Testing | 0/0 | Not started | - |