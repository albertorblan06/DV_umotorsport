# Architecture Research: Unit Testing, Refactoring & Scrum Integration

**Domain:** Autonomous Racing Kart Software Architecture (Testing & Refactoring Focus)
**Researched:** 2026-03-12
**Confidence:** HIGH

## Standard Architecture (Testable Extensions)

To support unit testing and algorithmic refactoring within the existing two-layer (Jetson AGX Orin + ESP32) architecture, the system boundaries must be decoupled from physical hardware using Hardware Abstraction Layers (HALs) and Dependency Injection.

### System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                 CI/CD & Scrum Pipeline Layer                 │
│  (GitHub Actions, SonarQube/Lizard, Coverage Dashboards)    │
├─────────────────────────────────────────────────────────────┤
│                         Jetson Orin                         │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────────────┐  │
│  │ ROS 2 Nodes  │  │ Core Logic   │  │ colcon test (C++) │  │
│  │ (Interfaces) │─▶│ (Algorithms) │◀─│ gtest / gmock     │  │
│  └──────────────┘  └──────────────┘  └───────────────────┘  │
├──────────────────────────────┬──────────────────────────────┤
│    UART Comm Bridge (Mockable via Virtual Serial/Ports)     │
├──────────────────────────────┴──────────────────────────────┤
│                            ESP32                            │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────────────┐  │
│  │ FreeRTOS Tasks│ │ PID / Logic  │  │ Unity/PlatformIO  │  │
│  │ (Scheduling) │─▶│ (Control)    │◀─│ Native Unit Tests │  │
│  └──────┬───────┘  └──────┬───────┘  └───────────────────┘  │
│         │                 │                                 │
│  ┌──────┴─────────────────┴───────┐                         │
│  │  Hardware Abstraction Layer    │◀── Mock Actuators       │
│  └────────────────────────────────┘                         │
└─────────────────────────────────────────────────────────────┘
```

### Component Responsibilities

| Component | Responsibility | Typical Implementation |
|-----------|----------------|------------------------|
| **Logic/Algorithm Cores** | Pure mathematical/planning logic (e.g., trajectory optimization, PID calculations). | Pure C++ classes with no ROS/FreeRTOS dependencies. Evaluated for strict $O(N)$ or $O(1)$ time complexity. |
| **Hardware Abstraction Layer (HAL)** | Wraps ESP32 hardware calls (PWM, DACs, GPIOs) and Orin interfaces (ZED SDK, UART). | Virtual interfaces (C++) or function pointers (C) injected at runtime. |
| **Test Runners** | Execute tests automatically in the build environment. | `gtest`/`gmock` for Orin via `colcon test`. `Unity` framework for ESP32 via PlatformIO. |
| **Metrics Collector** | Tracks code coverage and algorithmic complexity. | `gcov`/`lcov` for coverage, `lizard` for cyclomatic complexity checks during CI. |

## Recommended Project Structure

```
src/
├── kart_brain/                     # Orin ROS 2 Workspace
│   ├── src/
│   │   ├── core/                   # Pure C++ logic (Target for Big O optimization)
│   │   └── nodes/                  # ROS 2 wrappers injecting ROS deps into core
│   └── test/                       # gtest/gmock definitions testing `core/`
├── kart_medulla/                   # ESP32 Workspace
│   ├── lib/
│   │   ├── control/                # Pure C/C++ PID logic
│   │   └── hal/                    # Hardware Interfaces (PWM, UART)
│   ├── src/                        # FreeRTOS tasks and main.cpp
│   └── test/                       # PlatformIO native tests (Unity)
└── .github/workflows/              # Scrum/CI integration (Automated tests, linting)
```

### Structure Rationale

- **Separation of Core and Wrappers:** Separating algorithms from frameworks (ROS 2 / FreeRTOS) allows tests to run instantly on standard CI runners without launching Gazebo or physical hardware.
- **`test/` directories at the boundary:** Keeps test code isolated from production binaries, reducing payload size for the ESP32 and maintaining clean production builds for the Jetson.

## Architectural Patterns

### Pattern 1: Dependency Injection (Constructor/Setter Injection)

**What:** Passing dependencies (like hardware interfaces or configuration) into an object rather than having the object create them.
**When to use:** Whenever a module interacts with the ZED camera, UART, or ESP32 PWM/DACs.
**Trade-offs:** Adds slight overhead due to virtual tables (vptrs) in C++, but provides infinite testability.

**Example:**
```cpp
// Interface
class IMotorController {
public:
    virtual void setThrottle(float value) = 0;
    virtual ~IMotorController() = default;
};

// Production Implementation
class ESP32MotorController : public IMotorController {
    void setThrottle(float value) override { dacWrite(PIN, value); }
};

// Mock for Testing
class MockMotorController : public IMotorController {
public:
    MOCK_METHOD(void, setThrottle, (float), (override));
};

// Core Logic (Testable)
class TrajectoryPlanner {
    IMotorController* motor_;
public:
    TrajectoryPlanner(IMotorController* m) : motor_(m) {}
    void execute() { motor_->setThrottle(0.5f); } // Big O optimized
};
```

### Pattern 2: Pure Function Core, Imperative Shell

**What:** The core logic consists of pure functions (no side effects, outputs depend only on inputs). The "shell" (ROS 2 callbacks, FreeRTOS tasks) handles state and side effects.
**When to use:** Refactoring complex trajectory and perception logic to ensure strict Big O complexity boundaries and easy testing.
**Trade-offs:** Requires strict discipline. Data must be copied/passed into the core explicitly.

## Data Flow (Testing Pipeline)

### CI/CD Request Flow (Scrum Integration)

```
[Developer pushes PR (Scrum Task)]
    ↓
[CI Pipeline Triggered] 
    ↓
[Build Orin Workspace] → [Run gtest] → [Generate gcov Coverage]
    ↓                                        ↓
[Build ESP32 Firmware] → [Run Unity Tests natively (Host)] 
    ↓                                        ↓
[Complexity Analysis (Lizard)] ←─────────────┘
    ↓
[PR Status Checks (Pass/Fail) - Blocks Merge if Coverage < 80% or Big O > Threshold]
```

### Key Data Flows

1. **Mock Sensor Flow:** Test Framework → Injects mock Protobuf messages → Validates logic outputs in pure functions.
2. **Scrum Metrics Flow:** Source Code → Complexity Analyzer → CI Dashboard (Tracking technical debt reduction per Sprint).

## Suggested Build Order (Integration Strategy)

To safely implement these changes without breaking the existing kart, the build order MUST be strictly sequenced:

1. **Phase 1: CI/CD & Metric Baselines:** Setup GitHub Actions to compile current code and run complexity metrics. Establishes the "baseline" before refactoring.
2. **Phase 2: HAL Definition & Abstraction:** Create interfaces (`IMotorController`, `ISensorReader`) and wrap existing ESP32/Orin hardware calls without changing logic.
3. **Phase 3: Logic Decoupling:** Move PID and Trajectory logic into `core/` folders, stripped of FreeRTOS/ROS2 dependencies.
4. **Phase 4: Unit Test Implementation:** Write `gtest` and `Unity` tests against the now-isolated `core/` components using mock interfaces.
5. **Phase 5: Algorithmic Refactoring:** With tests protecting behavior, refactor the `core/` algorithms to achieve target Big O complexity.

## Anti-Patterns

### Anti-Pattern 1: Framework-Coupled Logic

**What people do:** Writing complex state machine logic directly inside a ROS 2 subscriber callback or a FreeRTOS task loop.
**Why it's wrong:** You cannot test the logic without spinning up the entire ROS 2 middleware or flashing the ESP32, making unit tests slow or impossible.
**Do this instead:** Extract the logic into a standard C++ class. Call the class method from the callback/task.

### Anti-Pattern 2: Testing over UART/Hardware for Unit Tests

**What people do:** Requiring the Orin to physically communicate with the ESP32 to validate basic logic.
**Why it's wrong:** This is an integration test, not a unit test. It is flaky, slow, and cannot be run in standard CI environments.
**Do this instead:** Mock the Protobuf serializers/UART bridge. Feed raw byte arrays into the core logic to simulate hardware communication in memory.

## Integration Points

### Internal Boundaries

| Boundary | Communication | Notes |
|----------|---------------|-------|
| Orin CI ↔ Codebase | `colcon test` | Requires `ament_cmake_gtest` setup in CMakeLists.txt. |
| ESP32 CI ↔ Codebase | PlatformIO Native | Tests must run on the `native` environment in `platformio.ini`, bypassing ESP-IDF dependencies during tests. |
| CI ↔ GitHub (Scrum) | GitHub Actions | Status checks should block PR merges if unit tests fail or if algorithmic complexity rules are violated. |

## Sources

- Clean Architecture principles (Dependency Rule)
- ROS 2 official testing documentation (`ament_cmake_gtest`)
- PlatformIO Unit Testing framework (Unity) documentation
- Embedded Software Testability (Hardware Abstraction Layer patterns)

---
*Architecture research for: Unit testing, refactoring, and Scrum adoption within a two-layer embedded system.*
*Researched: 2026-03-12*