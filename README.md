# DV_umotorsport

**DV_umotorsport** is an autonomous vehicle project focused on developing a robust, full autonomous navigation system for a kart. The project integrates high-performance computing (NVIDIA Jetson Orin) for perception and planning with real-time microcontrollers (ESP32) for low-level actuation and control.

## System Architecture

The architecture is built around two primary computing nodes communicating over a serial interface:

*   **High-Level Computing (NVIDIA Jetson Orin - ROS 2)**
    *   **Perception:** Processes data from depth cameras (e.g., ZED SDK) and LiDAR to detect cones, track objects, and generate local maps.
    *   **Planning:** Computes optimal trajectories and handles high-level path planning.
    *   **Middleware:** Utilizes ROS 2 for node communication, data logging (rosbags), and system management.

*   **Low-Level Control (ESP32 - FreeRTOS)**
    *   **Actuation:** Tracks steering setpoints and drives throttle/brake controllers via PWM/CAN.
    *   **Control Theory:** Implements high-frequency PID controllers for precise hardware manipulation.
    *   **Safety:** Manages hardware-level safe states (e.g., triggering emergency stops if serial communication is lost).

## Project Roadmap

The development workflow follows a structured roadmap to ensure reliability and performance:

1.  **Subsystem Stabilization & Integration Testing:** Ensuring perception, actuation, and communication systems are robust and documented independently.
2.  **Full Autonomous Navigation:** Establishing the complete architectural blueprints and system designs for autonomous software and hardware.
3.  **CI/CD & Project Management:** Establishing rigorous CI pipelines (Ruff, clang-tidy, ROS 2/ESP-IDF builds) and agile tracking boards.
4.  **Hardware Abstraction & Logic Decoupling:** Isolating core algorithms (PID, trajectory) from hardware and middleware dependencies via a Hardware Abstraction Layer (HAL).
5.  **Unit Testing & Performance Benchmarking:** Implementing GTest/PyTest, Unity tests for microcontrollers, and measuring execution latency via Google Benchmark.
6.  **End-to-End Validation & Regression Testing:** Holistic system validation using ROS bags and Hardware-In-the-Loop (HIL) testing.

## Getting Started

### Prerequisites

*   **ROS 2:** For running the high-level perception and planning nodes.
*   **ESP-IDF:** For building and flashing the low-level ESP32 firmware.
*   **Python 3.10+ / C++17:** Core languages used across the stack.
*   **uv / pip:** Python package management.

### Documentation

Comprehensive documentation for hardware, assembly, software architecture, and integration can be found in the `kart_docs/` directory. You can serve the documentation locally using MkDocs:

```bash
cd kart_docs
uv run mkdocs serve
```

## Contributing

We enforce strict code quality standards to ensure safety and reliability.

*   **C++:** Code is linted using `clang-tidy` with warnings treated as errors.
*   **Python:** Code is formatted and linted using `ruff`.

All pull requests must pass the automated GitHub Actions CI pipeline, which verifies formatting and validates builds across multiple isolated environments.
