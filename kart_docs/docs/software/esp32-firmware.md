# ESP32 Firmware

The ESP32 microcontroller serves as the critical bridge between high-level autonomous logic and the physical hardware actuators. The firmware is designed with an emphasis on real-time responsiveness and fail-safe operation.

## Responsibilities

The primary responsibilities of the ESP32 firmware include:
- Driving the steering motor via an H-bridge.
- Controlling throttle and braking systems through DACs and digital outputs.
- Monitoring safety conditions and enforcing emergency stops.
- Feeding back sensor data to the high-level ROS 2 system.

## Actuator Control

### Steering
The firmware receives a target steering angle from the ROS 2 planner. It implements a PID control loop, reading the current steering angle from an AS5600 magnetic angle sensor, and outputs a PWM signal to the Cytron MD30C H-bridge to drive the 24V steering motor to the desired position.

### Powertrain
Throttle control is managed by outputting precise analog voltages via a DAC to simulate the kart's hall-effect throttle pedal. The firmware ensures smooth acceleration and respects maximum speed limitations configured in the system.

### Braking
The braking system relies on a pneumatic actuator. The ESP32 triggers digital outputs to control the pneumatic valves, allowing for rapid and reliable engagement of the mechanical brakes when commanded.

## Safety Systems

The firmware implements several hardware-level safety features to prevent uncontrolled operation:

- **Heartbeat Monitoring:** The ESP32 continuously listens for a heartbeat signal from the high-level ROS 2 computer. If the heartbeat is lost or delayed beyond a configurable threshold, the firmware automatically transitions to a safe state, which includes cutting the throttle and applying the brakes immediately.
- **Limit Switches:** Physical limit switches on the steering rack are monitored to prevent over-rotation and damage to the steering mechanism.
- **Emergency Stop:** Integration with physical E-stop buttons allows immediate hard-cutoff of actuator power independent of the high-level software state.
