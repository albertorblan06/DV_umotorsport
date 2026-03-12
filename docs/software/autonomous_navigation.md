# Autonomous Navigation Software Architecture

## Overview
The autonomous navigation software stack for the DV_umotorsport vehicle is built upon ROS 2. It incorporates an advanced perception pipeline, localized planning, and robust control algorithms to maneuver the kart safely and effectively around the track. This document details the core software nodes and algorithmic approaches utilized in the navigation stack.

## Perception Pipeline
The perception system relies on camera data and LiDAR point clouds to build a comprehensive understanding of the kart's surroundings. The primary objectives are cone detection, color classification, and depth estimation.

- **Sensor Fusion**: LiDAR and camera data are time-synchronized.
- **Cone Detection**: Deep learning models identify racing cones from image streams.
- **Color Classification**: Bounding boxes from the camera are projected into the 3D space to classify cone types (e.g., yellow, blue, orange) which dictate the track boundaries.

## Track Limits and Boundary Mapping
Accurate delineation of the track is critical for safe navigation. The system employs geometric algorithms to map the drivable area.

### Delaunay Triangulation
Once the positions of the track cones are estimated in the local coordinate frame, Delaunay triangulation is applied to the set of cone coordinates.
- **Mesh Generation**: A triangular mesh is generated connecting all detected cones.
- **Edge Filtering**: Edges of the triangles that exceed a maximum distance threshold or cross the kart's longitudinal axis inappropriately are pruned.
- **Midpoint Extraction**: The algorithm computes the midpoints of the valid edges connecting the left (blue) and right (yellow) boundary cones. These midpoints formulate the target trajectory for the kart.

## Path Tracking and Control
The control subsystem is responsible for issuing steering and acceleration commands to follow the computed trajectory.

### ROS 2 Pure Pursuit Algorithm
The kart's path tracking relies on a custom implementation of the Pure Pursuit algorithm deployed as a ROS 2 node.
- **Lookahead Distance**: A dynamic lookahead distance is calculated based on the kart's current longitudinal velocity.
- **Curvature Calculation**: The node identifies a target point on the generated trajectory that corresponds to the lookahead distance. It then calculates the necessary steering angle curvature to intersect that target point from the vehicle's current position and heading.
- **Actuator Commands**: The calculated steering angles and corresponding target velocities are published as control commands to the low-level actuator management system.

## Node Architecture
- **perception_node**: Subscribes to `/camera/image_raw` and `/lidar/points`. Publishes `/perception/cones`.
- **mapping_node**: Subscribes to `/perception/cones` and `/odom`. Applies Delaunay triangulation and publishes `/planning/trajectory`.
- **pure_pursuit_node**: Subscribes to `/planning/trajectory` and `/odom`. Publishes `/control/cmd_vel` and `/control/steering`.
