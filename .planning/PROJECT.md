# DV_umotorsport

## What This Is

Autonomous racing kart developed by U Motorsport (Universidad Rey Juan Carlos, Madrid). The system detects track boundaries using computer vision, plans trajectories, and controls the kart in real time without a human driver. It features a two-layer architecture: a Jetson AGX Orin for high-level perception and planning, and an ESP32 for real-time PID control and actuator management.

## Current Milestone: v2.0 Full Remake

**Goal:** Solve issues from the root, enforce strict engineering standards (unit tests, low Big O, clean code), document all iterations, and adopt Scrum for a March 25th target.

**Target features:**
- Implement unit tests for all codebase components.
- Refactor existing code for simplicity and optimal algorithmic complexity (low Big O).
- Adopt Scrum methodology with documented iterations.
- Resolve underlying architectural issues from the root.
- Target completion deadline: March 25th.


## Core Value

Reliable, real-time autonomous control of a racing kart utilizing a unified computer vision pipeline and robust low-level actuator management.

## Requirements

### Validated

- ✓ YOLOv11 cone detection and ZED depth-based 3D localization
- ✓ ROS 2 colcon workspace setup with simulation capabilities
- ✓ ESP32 firmware with FreeRTOS handling 100Hz PID and comms
- ✓ UART communication bridge with Protobuf/nanopb

### Active

- [ ] Full end-to-end integration testing on the physical kart
- [ ] Autonomous trajectory planning and optimization based on cone localization
- [ ] Robust safety fail-safes and remote kill-switch integration

### Out of Scope

- Long-range cellular remote control (focusing on local autonomy and local dashboard)
- Non-standard racing environments (focusing on structured tracks with cones like autocross, hairpin, oval)

## Context

- **Compute Environment:** Jetson AGX Orin (JetPack 6.2.2, CUDA 12.6, TensorRT 10.3) and ESP32.
- **Framework:** ROS 2 Humble, Gazebo Fortress for simulation.
- **Communications:** Protobuf/nanopb over UART at 115200 baud.
- **Existing Setup:** High amount of existing code in `kart_brain`, `kart_medulla`, and `kart_docs`.

## Constraints

- **Real-time Latency**: The control task and communications must maintain 100Hz frequency.
- **Safety**: Fail-safe behaviors must be guaranteed in case of missed heartbeats (1 Hz liveness signal).
- **Hardware Limitations**: Interfacing directly with DACs and PWM signals for throttle, brake, and steering.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Two-Layer Architecture | Separates heavy AI computation (Orin) from strict real-time hardware control (ESP32) | — Pending |
| Protobuf over UART | Ensures structured, serialized messages with low overhead | — Pending |

---
*Last updated: 2026-03-12 Milestone v2.0 started*