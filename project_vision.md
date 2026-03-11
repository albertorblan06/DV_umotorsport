# UM-Driverless Autonomous Kart - Project Vision

## Overview
The `umotorsport` project is dedicated to developing a fully autonomous racing kart. The system is designed to navigate environments by detecting track boundaries (cones) and planning optimal trajectories in real-time. The architecture is split into high-level autonomous decision-making and low-level hardware actuation, ensuring modularity, safety, and high performance.

## System Architecture
The project is divided into three core repositories, each with a distinct responsibility:

1. **kart_brain (The High-Level Planner)**
   - **Hardware:** NVIDIA Orin
   - **Stack:** ROS2, C++, Python
   - **Role:** Handles computationally heavy tasks including the camera pipeline, machine learning inference (YOLOv11 with TensorRT optimization), trajectory planning, and the telemetry dashboard. It calculates the desired state of the kart and sends commands down to the Medulla.

2. **kart_medulla (The Low-Level Controller)**
   - **Hardware:** ESP32
   - **Stack:** C (ESP-IDF)
   - **Role:** Directly interfaces with the kart's physical hardware. It executes PID control loops for steering (target angle vs PWM) and acceleration/braking. It reads sensors via CAN/DAC, ensures hardware safety constraints (e.g., output limits, watchdog timers), and acts on the target commands received from the Brain.

3. **kart_docs (The Documentation)**
   - **Stack:** MkDocs, Markdown, YAML
   - **Role:** Maintains the Bill of Materials (BOM), hardware assembly instructions, sensor specifications, and overall system documentation.

## Current Focus
The immediate focus is stabilizing the foundational systems to support higher speeds and more reliable autonomy:
- Providing manual and remote control overrides via the dashboard for safe testing.
- Optimizing the perception pipeline (exporting YOLO models to TensorRT FP16) to achieve inference rates of 60-100 Hz.
- Tuning the low-level PID controllers on the ESP32 to eliminate oversteering and ensure precise mechanical actuation.
- Fixing infrastructure bugs, such as ROS2 node and `rviz` window accumulation.

## Long-Term Goals
- **Full Autonomous Loop:** Seamless integration from camera input to cone detection, trajectory generation, and physical actuation without human intervention.
- **Track Navigation:** Robust trajectory planning based on dynamic cone positions.
- **Campus Mapping:** Creating a map of the university for point-to-point autonomous navigation beyond closed track environments.

## Development Philosophy
- **Safety First:** The ESP32 Medulla must always have the final say on safety limits (clamping, watchdogs) in case the Orin Brain fails or lags.
- **Performance:** High-level code must be optimized for the Orin's architecture (using Tensor cores).
- **Professionalism:** All code, documentation, and agent interactions must remain strictly professional, concise, and entirely devoid of emojis.