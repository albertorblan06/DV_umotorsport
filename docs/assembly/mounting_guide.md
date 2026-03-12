# Assembly Documentation: Mounting Guide

## Overview
This document provides the standard operating procedures and mechanical constraints for assembling and mounting the autonomous navigation hardware suite onto the racing kart chassis. Adhering to these guidelines ensures system reliability, safety, and sensor accuracy.

## Mechanical Constraints

### Vibration Isolation
The racing kart chassis experiences significant high-frequency vibrations during operation.
- **Compute Unit**: Must be mounted using wire rope isolators or high-density rubber dampers to prevent structural damage to PCBs and ensure reliable USB connections.
- **ZED Camera**: Requires rigid mounting to avoid dynamic calibration shifts, but with a layer of stiff polyurethane to filter high-frequency resonance that could distort the image sensor readout.

### Thermal Management
- The main compute unit and motor controllers must be mounted in areas with adequate passive airflow. 
- Avoid placing heat-sensitive electronics directly adjacent to the combustion engine or exhaust manifold.
- All enclosed electronic boxes must feature IP65-rated breathable vents to prevent condensation while protecting against dust and moisture ingress.

## Mounting Instructions

### 1. ZED Camera Mounting
1. Locate the forward-most rigid cross-member of the front chassis.
2. Secure the custom CNC-machined aluminum bracket to the chassis using M6 aircraft-grade bolts. Apply medium-strength threadlocker to all bolts.
3. Attach the ZED camera to the bracket using the standard 1/4-20 tripod thread.
4. Verify the camera is perfectly level with the ground plane and precisely centered along the longitudinal axis of the kart.

### 2. Main Compute Unit
1. Position the compute unit enclosure behind the driver's seat, ensuring clearance from the engine bay.
2. Fasten the base plate to the chassis using four vibration isolation mounts.
3. Route all power and data cables through IP65 cable glands on the enclosure, ensuring drip loops are present to prevent water ingress.

### 3. Steering Actuator Assembly
1. Remove the stock steering wheel.
2. Slide the customized splined collar over the steering shaft.
3. Mount the stepper motor to the chassis using the heavy-duty steel mounting bracket.
4. Connect the motor shaft to the splined collar using the reinforced timing belt. Tension the belt to the specified limit to prevent skipping during rapid steering maneuvers.

### 4. ESP32 and Low-Level Electronics
1. Mount the ESP32 carrier board inside a secondary waterproof enclosure located near the actuator cluster to minimize cable run lengths.
2. Ensure all connections to the ESP32 (sensors, CAN bus, power) use locking connectors (e.g., JST-SM or Molex) to prevent disconnection under vibration.
3. Ground the enclosure and the ESP32 board to a common chassis ground point to minimize electromagnetic interference (EMI) from the ignition system.

## Final Verification
After all components are mounted:
- Perform a physical "shake test" on all brackets and enclosures.
- Verify that no cables are routed near sharp edges or moving parts (e.g., steering tie rods, pedals).
- Ensure all fasteners are marked with a torque stripe for visual inspection before each run.
