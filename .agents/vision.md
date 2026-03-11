# Project Vision

## Overview

The DV_umotorsport project develops a fully autonomous racing kart for U Motorsport (Universidad Rey Juan Carlos, Madrid). The system detects track boundaries (cones), plans optimal trajectories, and actuates in real-time. The architecture splits high-level autonomous decision-making from low-level hardware actuation for modularity, safety, and performance.

## System Architecture

Three subsystems in one monorepo:

1. **kart_brain (High-Level Planner)**
   - **Hardware:** NVIDIA Jetson Orin (AGX)
   - **Stack:** ROS 2, C++, Python
   - **Role:** Camera pipeline, ML inference (YOLOv11 + TensorRT), trajectory planning, telemetry dashboard. Calculates desired kart state and sends commands to the Medulla.

2. **kart_medulla (Low-Level Controller)**
   - **Hardware:** ESP32
   - **Stack:** C (ESP-IDF)
   - **Role:** PID control loops for steering (target angle vs PWM) and acceleration/braking. Reads sensors via I2C/DAC, enforces hardware safety constraints (output limits, watchdog timers), acts on target commands from the Brain.

3. **kart_docs (Documentation)**
   - **Stack:** MkDocs, Markdown, YAML
   - **Role:** Bill of Materials (BOM), hardware assembly instructions, sensor specs, system documentation. Live site: https://um-driverless.github.io/kart_docs/

## Current Focus

Stabilizing foundational systems for higher speeds and more reliable autonomy:
- Manual and remote control overrides via the dashboard for safe testing
- Optimizing the perception pipeline (YOLO to TensorRT FP16) for 60-100 Hz inference
- Tuning low-level PID controllers on the ESP32 for precise mechanical actuation
- Fixing infrastructure bugs (process accumulation, zombie processes on Orin)

## Long-Term Goals

- **Full Autonomous Loop:** Camera input to cone detection to trajectory generation to physical actuation, no human intervention
- **Track Navigation:** Robust trajectory planning from dynamic cone positions
- **Campus Mapping:** University map for point-to-point autonomous navigation beyond closed tracks

## Development Philosophy

- **Safety First:** The ESP32 Medulla always has final say on safety limits (clamping, watchdogs) in case the Orin Brain fails or lags.
- **Performance:** High-level code optimized for the Orin's architecture (Tensor cores, CUDA 12.6).
- **Professionalism:** All code, documentation, and agent interactions are strictly professional, concise, and devoid of emojis.
