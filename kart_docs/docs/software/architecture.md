# Software Architecture

The software architecture of the driverless kart is designed to be modular, robust, and extensible, ensuring safe and reliable autonomous operation. The system is split across high-level decision making and low-level control.

## Overview

The overall architecture is divided into two primary subsystems:
1. **High-Level Control (ROS 2):** Runs on an NVIDIA Jetson AGX Orin. It is responsible for perception, mapping, planning, and telemetry.
2. **Low-Level Control (ESP32):** Runs on an ESP32 microcontroller. It handles direct actuator control (steering, throttle, braking) and enforces safety limits.

## Repositories

- **Current ROS 2 Implementation (2025):** [UM-Driverless/KART_SW](https://github.com/UM-Driverless/KART_SW)
- **Legacy Python Implementation (2024):** [UM-Driverless/driverless](https://github.com/UM-Driverless/driverless)

## Core Subsystems

### Perception and Mapping
The perception pipeline leverages a Stereolabs ZED2 camera and YOLOv11 to detect track boundaries and traffic cones. These detections are converted into a 3D local coordinate frame to map the environment in real time.

### Planning (AUTO-02)
The planning subsystem receives the localized cone map and computes feasible racing lines. This component ensures the kart remains within track limits while optimizing for the best path based on vehicle dynamics constraints.

### Telemetry (TELE-01)
A comprehensive telemetry system is integrated to monitor the kart's state. A ROS 2 dashboard is used to display current operational modes, vehicle speeds, active camera feeds, and real-time sensor data, providing operators with full situational awareness during runs.

### Low-Level Integration
The ROS 2 stack communicates with the ESP32 firmware via a dedicated bridge. The high-level planner sends target steering angles and target speeds, which the ESP32 translates into specific PWM, DAC, and digital signals.
