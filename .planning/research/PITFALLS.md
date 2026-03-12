# Domain Pitfalls

**Domain:** Autonomous Robotics (ROS 2 / Hardware Control)
**Researched:** 2026-03-12

## Critical Pitfalls

Mistakes that cause rewrites or major issues when adding unit tests, refactoring, and adopting Scrum.

### Pitfall 1: Mocking Hardware Incorrectly (Testing)
**What goes wrong:** Unit tests pass perfectly, but the physical robot crashes immediately.
**Why it happens:** Tests are written against overly simplistic mocks of hardware interfaces (ESP32, sensors) that do not accurately reflect real-world noise, latency, or failure modes (e.g., dropped UART packets, sensor drift).
**Consequences:** False confidence in the codebase; integration tests on the physical kart fail catastrophically.
**Prevention:** Use Gazebo Fortress for hardware-in-the-loop (HITL) or software-in-the-loop (SITL) testing instead of just basic unit testing for ROS nodes. When mocking, inject noise and simulate dropped packets (especially for the UART/Protobuf bridge).
**Detection:** Tests always pass instantly with zero variance, but integration testing consistently reveals edge cases.

### Pitfall 2: Premature Algorithmic Optimization (Big O)
**What goes wrong:** Weeks are spent optimizing a path-planning algorithm from O(N^2) to O(N log N), but the system latency remains unchanged.
**Why it happens:** Developers optimize code before profiling the system. In robotics, the bottleneck is often I/O latency (UART communication at 115200 baud, sensor readout, ROS 2 DDS overhead) or GPU inference (YOLOv11), not CPU algorithmic complexity.
**Consequences:** Wasted development time; code becomes significantly harder to read and maintain for negligible performance gains.
**Prevention:** Profile first. Use tools like `ros2 trace` or `valgrind` to identify actual bottlenecks. Only optimize Big O if the specific component is proven to be the critical path.
**Detection:** Complex code PRs that don't include benchmarks proving a real-world latency reduction.

### Pitfall 3: Forcing Software Sprints on Hardware Realities (Scrum)
**What goes wrong:** The team fails to deliver the sprint goal because a physical part broke or an integration issue took 3 days to debug.
**Why it happens:** Standard 2-week software Scrum assumes predictable velocity and zero physical constraints. Hardware integration and testing on a physical kart are inherently unpredictable.
**Consequences:** Demoralized team, meaningless sprint velocity metrics, and rushed, unsafe physical testing to "meet the sprint goal."
**Prevention:** Adapt Scrum for hardware (Hardware Agile). Decouple software simulation sprints from physical integration sprints. Always include buffer time for "hardware gremlins" in the sprint backlog.
**Detection:** Sprints consistently carry over physical integration tasks; team complains that sprint goals are unrealistic.

## Moderate Pitfalls

### Pitfall 1: Testing ROS 2 Nodes in Isolation Only
**What goes wrong:** Nodes work individually but fail to communicate due to QoS (Quality of Service) mismatches.
**Prevention:** Ensure integration tests cover the entire pipeline (Perception -> Planning -> Control) with the exact QoS settings used on the physical kart.

### Pitfall 2: Over-Refactoring the ESP32 Firmware
**What goes wrong:** Refactoring the ESP32 code for "clean architecture" introduces jitter to the 100Hz PID control loop.
**Prevention:** Keep embedded code straightforward. Avoid dynamic memory allocation or complex inheritance trees in the FreeRTOS tasks.

## Phase-Specific Warnings

| Phase Topic | Likely Pitfall | Mitigation |
|-------------|---------------|------------|
| Testing Setup | Creating flaky tests that fail randomly | Ensure deterministic time in ROS 2 tests (use `use_sim_time`). |
| Refactoring | Breaking the YOLOv11/ZED perception pipeline | Write characterization tests (capture current behavior) *before* touching the CV code. |
| Scrum Adoption | Spending too much time in planning meetings | Keep ceremonies short; focus on actionable tasks rather than perfect story pointing. |

## Sources

- Context: Project constraints (100Hz real-time, UART bridge, ROS 2 Humble).
- Best Practices: ROS 2 Testing guidelines, Agile for Hardware principles.
