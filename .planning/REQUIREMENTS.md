# DV_umotorsport Requirements

## Current Milestone (v2.0 Full Remake)

### CI & Metrics
- [x] **METR-01**: PR CI pipeline executes automated tests and linters
- [x] **METR-02**: Static code analysis (clang-tidy, Ruff) fails CI on violations
- [ ] **METR-03**: Automated ROS Bag regression tests execute against computer vision pipeline

### Testing & Hardware Abstraction
- [ ] **TEST-01**: Hardware Abstraction Layer (HAL) abstracts ESP32 and Orin hardware interfaces
- [ ] **TEST-02**: ROS 2 Jetson logic is validated via GTest/PyTest test suites
- [ ] **TEST-03**: ESP32 PID and comms logic is validated via Unity unit tests
- [ ] **TEST-04**: Hardware-in-the-Loop (HIL) testing infrastructure validates end-to-end behavior

### Refactoring & Performance
- [ ] **PERF-01**: PID and Trajectory planning logic is decoupled into a pure C/C++ core
- [ ] **PERF-02**: Algorithmic refactoring reduces computational complexity (Big O) of core algorithms
- [ ] **PERF-03**: Google Benchmark validates latency and algorithmic complexity constraints in CI

### Scrum Methodology
- [ ] **SCRU-01**: Project backlog and iterations are tracked via lightweight GitHub Projects boards

## Future / Deferred
- Decoupling software sprints from hardware integration sprints (Deferred)
- Heavy Enterprise Scrum (Jira) (Deferred)

## Out of Scope
- Full physical Kart test per PR (dangerous, blocks fast development)

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| METR-01 | Phase 3 | Complete |
| METR-02 | Phase 3 | Complete |
| METR-03 | Phase 6 | Pending |
| TEST-01 | Phase 4 | Pending |
| TEST-02 | Phase 5 | Pending |
| TEST-03 | Phase 5 | Pending |
| TEST-04 | Phase 6 | Pending |
| PERF-01 | Phase 4 | Pending |
| PERF-02 | Phase 5 | Pending |
| PERF-03 | Phase 5 | Pending |
| SCRU-01 | Phase 3 | Pending |

