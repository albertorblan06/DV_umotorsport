# Integration and Lap Completion

## Introduction
The successful execution of an autonomous mission demands precise integration between all subsystems and reliable logic to track mission progress. This document outlines the end-to-end testing procedures and the lap completion algorithms for the autonomous kart.

## End-to-End Integration Testing
Testing full autonomous capabilities requires a controlled and phased approach.

- **System Startup**: Ensure all sensor drivers, low-level controllers, and ROS 2 nodes are launched correctly without initialization errors.
- **Static Validation**: Verify that perception nodes accurately classify cones and that the tracking module correctly generates trajectories while the vehicle is stationary.
- **Dynamic Validation**: Engage the low-level controllers and observe the kart's behavior at low speeds, confirming that pure pursuit commands map correctly to steering and throttle actuation.

## Lap Completion Logic
To fulfill mission constraints, the system must accurately detect when the kart has completed a full lap. This involves combining multiple signals to ensure robustness against sensor dropouts.

### Start and Finish Line Detection
The primary mechanism relies on identifying the specific visual markers of the start and finish lines.
- **Orange Cone Gates**: The start and finish zones are delineated by large orange cones. The perception pipeline identifies these features to register the crossing of the gate.
- **Temporal Debouncing**: To prevent multiple triggers from a single pass, a strict temporal debounce filter is applied to the gate detection signal.

### SLAM Loop Closure
Simultaneous Localization and Mapping (SLAM) is used to corroborate the physical gate detection.
- **Map Correlation**: As the vehicle traverses the track, the SLAM system incrementally builds a map of the environment.
- **Loop Closure Detection**: When the kart returns to an area previously mapped (the start zone), the SLAM system performs a loop closure. This topological match acts as a secondary confirmation that a full lap has been completed.

### Distance Heuristics
A fail-safe mechanism using distance metrics guarantees lap tracking even if visual markers are missed.
- **Odometry Tracking**: The navigation stack accumulates the total distance traveled based on wheel odometry and IMU integration.
- **Minimum Distance Threshold**: A lap is only considered valid if the integrated distance exceeds a predefined threshold configured for the specific track layout.

## Mission State Machine
The integration of these detection methods is handled by a state machine node.
- **STATE_START**: Vehicle is stationary at the starting gate.
- **STATE_RACING**: Vehicle crosses the starting gate and is actively tracking the path.
- **STATE_FINISHED**: The system confirms a lap completion via gate detection combined with loop closure or distance heuristics, prompting the kart to decelerate safely.
