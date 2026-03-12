# Hardware Documentation: Sensors and Actuators

## Overview
This document details the primary hardware components utilized for the full autonomous navigation system of the racing kart. It covers the sensor suite and the actuation mechanisms, ensuring robust real-time data acquisition and precise control.

## Sensors

### ZED Camera
The ZED stereo camera is the primary vision sensor for the autonomous pipeline. It provides high-resolution, high-framerate depth mapping and visual odometry.
- **Mounting Position**: Front chassis, elevated to provide an unobstructed field of view.
- **Interface**: USB 3.0 to the main compute unit.
- **Power**: Sourced directly from the primary sensor power distribution board to ensure stable voltage.
- **Data Flow**: Streams RGB and depth channels to the perception node for object detection, lane tracking, and localization.

### Additional Sensors
- **IMU (Inertial Measurement Unit)**: Used for high-frequency orientation and acceleration tracking. It supplements the visual odometry provided by the ZED camera.
- **Wheel Encoders**: Provide precise wheel speed and distance measurements, crucial for dead reckoning and state estimation.

## Actuators

### Steering Actuation
The steering mechanism is controlled via a high-torque stepper motor directly coupled to the steering column.
- **Controller**: Driven by a dedicated motor controller which receives CAN or PWM signals from the low-level processing unit.
- **Feedback**: Absolute rotary encoders on the steering column provide closed-loop feedback to ensure exact angular positioning.

### Braking Actuation
Braking is achieved through a linear linear actuator that directly manipulates the hydraulic brake master cylinder.
- **Failsafe**: A mechanical return spring and normally-closed solenoid valve ensure the brakes default to an engaged state in the event of power loss.

### Throttle Actuation
The throttle is controlled via a servomotor attached to the throttle body.
- **Redundancy**: Dual potentiometers provide redundant positional feedback, monitored constantly by the safety controller to detect signal discrepancies.

## ESP32 Wiring and Integration
The ESP32 microcontroller serves as the low-level bridge between the high-level autonomy software and the physical hardware layer.
- **Communication Protocol**: The ESP32 communicates with the main compute unit via serial/USB and interfaces with the motor controllers using CAN bus.
- **Pin Configuration**:
  - `GPIO 16, 17`: CAN TX/RX for motor controllers.
  - `GPIO 32, 33`: Serial interface for debugging and telemetry.
  - `GPIO 25, 26`: Analog inputs for redundant throttle feedback.
- **Isolation**: All logic-level signals from the ESP32 to high-power actuators are passed through optoisolators to prevent voltage spikes from damaging the microcontroller.
