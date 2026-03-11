# DV_umotorsport

Autonomous racing kart developed by **U Motorsport** (Universidad Rey Juan Carlos, Madrid). The system detects track boundaries using computer vision, plans trajectories, and controls the kart in real time -- no human driver required.

## Architecture

The platform splits into two layers connected over UART:

| Layer | Hardware | Role |
|---|---|---|
| **kart_brain** | NVIDIA Jetson AGX Orin | Perception, planning, control, telemetry |
| **kart_medulla** | ESP32 WROOM 32 | Real-time PID, actuator driving, sensor reading |

```
ZED Camera --> YOLO Detector --> 3D Cone Localizer --> Planner --> Protobuf/UART --> ESP32 --> Actuators
                                                                                      ^
                                                                               AS5600 steering feedback
```

A third module, **kart_docs**, hosts the project documentation site.

## Repository Structure

```
DV_umotorsport/
├── kart_brain/       # ROS 2 Humble workspace (Python + C++)
├── kart_medulla/     # ESP32 firmware (C, ESP-IDF via PlatformIO)
├── kart_docs/        # MkDocs Material documentation site
├── .agents/          # Unified knowledge base for developers and AI agents
├── .planning/        # GSD workflow configuration
├── TODO.md           # Prioritized task list
└── stuff.md          # Unstructured notes and links
```

## kart_brain

ROS 2 colcon workspace running on the Jetson Orin. 9 packages:

| Package | Description |
|---|---|
| `kart_perception` | YOLOv11 cone detection + ZED depth-based 3D localization |
| `kart_bringup` | Launch files for autonomous, teleop, and dashboard modes |
| `kart_sim` | Gazebo Fortress simulation (oval, hairpin, autocross tracks) |
| `kb_coms_micro` | C++ serial bridge: ROS 2 topics <-> ESP32 UART |
| `kb_interfaces` | Custom ROS 2 message definitions |
| `kb_serial_driver_lib` | Low-level USB serial driver |
| `kb_dashboard` | Web dashboard (port 8080, WebSocket) |
| `joy_to_cmd_vel` | Joystick input to Twist commands |

Also includes a 2D simulator (`scripts/sim2d/`) for training neural controllers using genetic algorithms and CMA-ES, and a YOLO training pipeline (`training/`) that pulls from FSOCO, Roboflow, and MIT Driverless datasets.

### Quick Start (Orin)

```bash
# Build
cd kart_brain && colcon build --symlink-install
source install/setup.bash

# Autonomous mode
ros2 launch kart_bringup autonomous.launch.py

# Simulation
ros2 launch kart_sim simulation.launch.py track:=autocross

# Dashboard only (safe for testing)
ros2 launch kart_bringup dashboard.launch.py
```

## kart_medulla

ESP32 firmware built with ESP-IDF via PlatformIO. Runs 3 FreeRTOS tasks:

| Task | Frequency | Role |
|---|---|---|
| comms | 100 Hz | UART RX/TX with Orin (protobuf frames) |
| control | 100 Hz | PID steering control + actuator output |
| heartbeat | 1 Hz | Liveness signal to Orin |

### Hardware

| Actuator | GPIO | Type |
|---|---|---|
| Throttle | 26 | DAC (0-255) |
| Brake | 25 | DAC (0-255) |
| Steering PWM | 27 | LEDC PWM |
| Steering DIR | 14 | Digital |
| AS5600 SDA/SCL | 21/22 | I2C (400 kHz) |

### Build & Flash

```bash
cd kart_medulla
pio run                    # Build
pio run -t upload          # Flash
pio device monitor -b 460800  # Serial monitor
```

## kart_docs

MkDocs Material site with assembly guides, bill of materials, datasheets, and software docs. Deployed to GitHub Pages via CI.

**Live site:** https://um-driverless.github.io/kart_docs/

```bash
cd kart_docs
uv run mkdocs serve        # Local preview at localhost:8000
```

## Tech Stack

- **Compute:** Jetson AGX Orin (JetPack 6.2.2, CUDA 12.6, TensorRT 10.3), ESP32 (ESP-IDF)
- **Perception:** YOLOv11 (Ultralytics), ZED 2 stereo camera, TensorRT FP16 target
- **Framework:** ROS 2 Humble, Gazebo Fortress
- **Comms:** Protobuf/nanopb over UART (115200 baud, CRC8 framing)
- **Languages:** Python, C++, C
- **Build:** colcon (brain), PlatformIO (medulla), uv + MkDocs (docs)
- **Chassis:** Tony Kart Extreme

## Documentation

All project knowledge is centralized in `.agents/`. Start with [`.agents/README.md`](.agents/README.md).

Key docs:

| File | Content |
|---|---|
| `.agents/architecture.md` | System architecture, node graphs, protocol spec |
| `.agents/medulla.md` | ESP32 reference: pins, tasks, safety, debugging |
| `.agents/vision.md` | Project goals and long-term roadmap |
| `.agents/errors.md` | Error log with 26+ entries and prevention rules |
| `.agents/simulation.md` | Gazebo setup and known issues |
| `.agents/orin_environment.md` | Jetson hardware specs, SSH, software versions |

## License

Private repository. All rights reserved.
