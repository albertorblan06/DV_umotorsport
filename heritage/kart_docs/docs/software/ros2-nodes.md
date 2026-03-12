# ROS 2 Nodes

The high-level software stack is built using ROS 2, providing a distributed and real-time capable environment for the kart's autonomous operations.

## Perception Nodes

- **Camera Driver Node:** Interfaces with the ZED2 stereo camera to publish raw image streams and depth information.
- **Detection Node:** Subscribes to image topics and runs inference using YOLOv11 to identify cones and track markers at a frequency of 15Hz or higher.
- **Localization Node:** Converts 2D bounding boxes and depth data into a local 3D coordinate system, constructing a dynamic map of the immediate environment.

## Planning Nodes (AUTO-02)

The planning stack is responsible for calculating safe and efficient trajectories.

- **Path Planner Node:** Subscribes to the localized map and computes feasible racing lines. It accounts for track boundaries defined by localized cones and ensures that the generated path conforms to the kart's dynamic limits.
- **Control Node:** Translates the planned trajectory into target steering angles and target speeds. These targets are then published to the hardware bridge.

## Telemetry and Dashboard (TELE-01)

Monitoring the system state is critical for safe operation and debugging.

- **Telemetry Node:** Aggregates data from various subsystems, including current speed, steering angle feedback, and system health status.
- **Dashboard Interface:** Subscribes to telemetry topics and camera feeds to provide a unified graphical interface. Operators can view current state, speeds, and live camera feeds to evaluate performance and ensure safety.

## Hardware Bridge

- **Microcontroller Interface Node:** Acts as the communication bridge between the ROS 2 network and the ESP32. It serializes target commands into a format understood by the low-level firmware and deserializes sensor feedback back into ROS 2 topics.
