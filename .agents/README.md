# Agent Entry Point

**Read this file first before doing anything.** This is the source of truth for all AI agents and human developers working on the DV_umotorsport sandbox.

## Project Overview

Autonomous racing kart developed by U Motorsport (Universidad Rey Juan Carlos, Madrid). Three subsystems in one monorepo:

| Directory | Hardware | Stack | Role |
|-----------|----------|-------|------|
| `kart_brain/` | NVIDIA Jetson Orin | ROS 2, C++, Python | Perception (YOLO + depth), planning, dashboard, comms |
| `kart_medulla/` | ESP32 | C (ESP-IDF) | PID control, actuators, sensors, safety |
| `kart_docs/` | -- | MkDocs, YAML | Documentation site, BOM, assembly guides |

## Required Reading (in order)

1. **`.agents/vision.md`** -- Project vision, goals, philosophy
2. **`.agents/architecture.md`** -- System architecture, node graphs, protocols, message types
3. **`.agents/methodology.md`** -- Development rules, GSD workflow, commit policy
4. **`.agents/errors.md`** -- Past mistakes and prevention rules (review before every session)
5. **Environment guide for your target:**
   - Orin (real hardware): `.agents/orin_environment.md`
   - ESP32 firmware: `.agents/medulla.md`
   - Simulation (VM): `.agents/simulation.md` + `.agents/vm_environment.md`
    - Orin reflash: `.agents/orin_flash_guide.md`
6. **Other references:**
   - `.agents/scratchpad.md` -- Working notes on simulation, training experiments
   - `.agents/investigation_rviz_accumulation.md` -- RViz accumulation bug investigation

## Key Directories

| Path | What |
|------|------|
| `.agents/` | This directory -- all agent/dev knowledge |
| `.planning/` | GSD workflow state, config, roadmaps |
| `kart_brain/src/` | ROS 2 packages (perception, bringup, sim, dashboard, comms) |
| `kart_brain/models/` | YOLO weights |
| `kart_brain/scripts/` | Utility scripts, 2D simulator |
| `kart_brain/proto/` | Protobuf definitions + generated code |
| `kart_medulla/main/` | ESP32 entry point (app_main) |
| `kart_medulla/components/` | ESP32 libraries (km_act, km_coms, km_pid, km_sdir, ...) |
| `kart_docs/docs/` | MkDocs documentation source |

## Quick Commands

```bash
# kart_brain -- build & run
ssh orin
cd ~/kart_brain && colcon build
ros2 launch kart_bringup autonomous.launch.py
~/kart_brain/run_live.sh              # live perception

# kart_medulla -- flash ESP32 (from Orin)
cd ~/Desktop/kart_medulla
~/.local/bin/pio run --target upload --environment esp32dev --upload-port /dev/ttyUSB0

# kart_docs -- local dev server
cd kart_docs && uv run mkdocs serve

# Simulation (VM)
ssh utm
ros2 launch kart_sim simulation.launch.py
```

## Workflow

This project uses **GSD (Get Shit Done)** for structured planning and execution. See `.agents/methodology.md` for details. Key commands:

- `/gsd-new-project` -- Create project roadmap
- `/gsd-plan-phase` -- Plan a phase
- `/gsd-execute-phase` -- Execute a phase
- `/gsd-settings` -- Configure GSD

## Rules

1. No emojis. Professional, concise, direct.
2. Read `.agents/errors.md` before every session.
3. Commit after every meaningful change.
4. Document every error in `.agents/errors.md`.
5. A change is NOT done until validated on the target machine.
6. Never run destructive commands without explicit confirmation.
7. When in doubt, ask -- do not assume.
