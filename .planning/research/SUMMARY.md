# Project Research Summary

**Project:** DV_umotorsport (Milestone: v2.0 Full Remake)
**Domain:** Autonomous Vehicle Software Engineering (Testing, Refactoring, Scrum)
**Researched:** 2026-03-12
**Confidence:** HIGH

## Executive Summary

The DV_umotorsport v2.0 Full Remake focuses on establishing a robust engineering culture with unit testing, refactoring for Big O efficiency, and lightweight Scrum. The system operates on a two-layer architecture: a Jetson AGX Orin running ROS 2 for perception and planning, and an ESP32 handling real-time hardware control. Experts build these systems by strictly decoupling pure mathematical algorithms from hardware and middleware frameworks using Hardware Abstraction Layers (HALs) and Dependency Injection. 

The recommended approach establishes a pure function core wrapped by an imperative shell. By isolating the logic, the team can use standard unit testing tools (GTest for C++, Unity for ESP32) to execute fast, deterministic tests on continuous integration (CI) runners without needing the physical kart. Performance can then be empirically validated using Google Benchmark to ensure the 100Hz real-time latency requirement is met.

Key risks include mocking hardware incorrectly (leading to false confidence in tests) and premature algorithmic optimization (wasting time on non-bottlenecks). To mitigate these, the team must first baseline current performance with profiling tools, introduce simulated noise and dropped packets in their mocks, and strictly decouple software simulation sprints from unpredictable physical hardware integration sprints.

## Key Findings

### Recommended Stack

The stack emphasizes native integration with existing tools and lightweight profiling.

**Core technologies:**
- **GTest / GMock & Unity:** C++ Unit Testing — Native to ROS 2 (`ament_cmake_gtest`) and ESP-IDF respectively. Essential for isolated testing.
- **Google Benchmark:** Algorithmic Complexity — Features `SetComplexityN` to automatically calculate and mathematically prove asymptotic complexity (e.g., O(N)) for refactored components.
- **GitHub Projects:** Scrum Tracking — Low friction, avoids the overhead of Jira while tightly coupling with pull requests and issues.
- **clang-tidy / Ruff:** Linting & Static Analysis — Enforces clean code standards and catches memory bugs early in the CI pipeline.

### Expected Features

**Must have (table stakes):**
- ROS 2 GTest/PyTest Integration — Essential for validating planning/vision logic safely.
- ESP32 Unity Unit Testing — Required to test PID and comms logic without the physical kart.
- Automated CI/CD Pipeline — Prevents regressions by running tests and linters on every PR.
- Static Code Analysis — Enforces modern standards automatically.
- Scrum Artifacts & Rituals — Lightweight backlog and sprint boards for the tight deadline.

**Should have (competitive):**
- Big O / Performance Benchmarking in CI — Ensures refactoring actually improves latency.
- Automated ROS Bag Regression Tests — Validates the computer vision pipeline holistically.

**Defer (v2+):**
- Hardware-in-the-Loop (HIL) Testing — High setup cost, defer until Software-in-the-Loop (SIL) is solid.
- Full Kart Test per PR — Dangerous and blocks fast development.
- Heavy Enterprise Scrum (Jira) — Unnecessary overhead.

### Architecture Approach

The architecture adopts a Clean Architecture pattern with a Pure Function Core and Imperative Shell to maximize testability.

**Major components:**
1. **Logic/Algorithm Cores** — Pure C/C++ mathematical and planning logic (e.g., trajectory optimization, PID) separated from ROS/FreeRTOS.
2. **Hardware Abstraction Layer (HAL)** — Virtual interfaces wrapping ESP32 hardware calls (PWM, UART) and Orin interfaces (ZED SDK).
3. **Test Runners & Metrics** — Automated execution (`colcon test`, native PlatformIO) tracking coverage and complexity via CI.

### Critical Pitfalls

1. **Mocking Hardware Incorrectly:** Simplistic mocks ignore real-world noise and dropped packets. *Avoid by injecting simulated noise/failures and using SITL (Gazebo).*
2. **Premature Algorithmic Optimization:** Optimizing CPU complexity when I/O or DDS latency is the real bottleneck. *Avoid by profiling first (ros2 trace) and only optimizing the proven critical path.*
3. **Forcing Software Sprints on Hardware Realities:** Physical breakages ruin standard 2-week software sprint goals. *Avoid by decoupling software simulation sprints from hardware integration sprints, and always including buffer time.*

## Implications for Roadmap

Based on research, a strict bottom-up integration strategy is required to safely refactor the kart without breaking existing functionality.

### Phase 1: CI/CD & Metric Baselines
**Rationale:** You cannot improve what you cannot measure. A baseline is needed before any code is modified.
**Delivers:** GitHub Actions CI pipeline, linting checks, and initial complexity/coverage metrics.
**Addresses:** Automated CI/CD Pipeline, Static Code Analysis.
**Avoids:** Premature Algorithmic Optimization.

### Phase 2: HAL Definition & Abstraction
**Rationale:** Hardware dependencies must be abstracted before logic can be extracted and tested.
**Delivers:** C++ Interfaces (`IMotorController`, `ISensorReader`) that wrap existing hardware calls without altering the business logic.
**Uses:** Dependency Injection architectural pattern.
**Implements:** Hardware Abstraction Layer (HAL).

### Phase 3: Logic Decoupling & Unit Test Implementation
**Rationale:** Logic must be isolated and protected by tests before attempting complex Big O refactoring.
**Delivers:** PID and Trajectory logic moved to isolated `core/` directories, with full GTest and Unity coverage utilizing mock interfaces.
**Addresses:** ROS 2 GTest, ESP32 Unity Tests.
**Avoids:** Framework-Coupled Logic, Testing ROS 2 nodes in isolation only.

### Phase 4: Algorithmic Refactoring & Benchmarking
**Rationale:** With tests protecting the behavior, the team can safely optimize algorithms to meet the 100Hz real-time requirement.
**Delivers:** Refactored algorithms and Google Benchmark integration in CI to prevent latency regressions.
**Uses:** Google Benchmark, C++ Core Logic.
**Addresses:** Big O / Performance Benchmarking in CI.

### Phase Ordering Rationale

- **Dependencies:** CI and metrics must exist before code changes (Phase 1). Hardware abstraction (Phase 2) is a prerequisite for logic decoupling (Phase 3). Refactoring (Phase 4) is unsafe without the unit tests written in Phase 3.
- **Architecture:** Progressively moves the system towards a Pure Function Core by wrapping the messy imperative shell first.
- **Pitfalls:** This order guarantees that refactoring is driven by proven bottlenecks and protected by rigorous, mock-driven tests rather than blind optimization.

### Research Flags

Phases likely needing deeper research during planning:
- **Phase 2:** Defining the exact mock boundaries and Protobuf serialization over the UART bridge between the Jetson and ESP32.
- **Phase 4:** Establishing exact Big O benchmarking baseline thresholds for the ZED perception and trajectory planning nodes.

Phases with standard patterns (skip research-phase):
- **Phase 1 & 3:** Standard ROS 2 GTest, PlatformIO Unity, and GitHub Actions setups are well-documented.

## Confidence Assessment

| Area | Confidence | Notes |
|------|------------|-------|
| Stack | HIGH | Based on official ROS 2 Humble and ESP-IDF documentation. |
| Features | HIGH | Matches industry standards for autonomous robotics software pipelines. |
| Architecture | HIGH | Clean Architecture and Dependency Injection are proven patterns for testing embedded systems. |
| Pitfalls | HIGH | Common issues derived from hardware integration realities. |

**Overall confidence:** HIGH

### Gaps to Address

- **UART Bridge Mocking:** Research was inconclusive on the exact library/pattern to mock the specific Protobuf-over-UART communication efficiently in standard CI without writing a custom virtual serial port emulator. Needs validation during implementation.

## Sources

### Primary (HIGH confidence)
- ROS 2 Humble Testing Documentation — `ament_cmake_gtest` and Python testing.
- Google Benchmark GitHub — Features and integration.
- ESP-IDF Unit Testing with Unity — Embedded testing on ESP32.

### Secondary (MEDIUM confidence)
- Clean Architecture principles (Dependency Rule) — Adapting pure software patterns to mixed hardware/ROS environments.
- Agile for Hardware principles — Adjusting Scrum for physical robotics constraints.

---
*Research completed: 2026-03-12*
*Ready for roadmap: yes*
