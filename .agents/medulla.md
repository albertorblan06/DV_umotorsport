# ESP32 Medulla Reference

Agent and developer reference for the `kart_medulla/` subsystem -- the ESP32-based low-level controller.

## Repository Structure

**ESP-IDF project with PlatformIO. Source in `main/`, custom libraries in `components/`.**

```
kart_medulla/
├── main/
│   ├── main.c              # ESP-IDF entry point (app_main + FreeRTOS tasks)
│   ├── sketch.cpp          # Legacy Bluepad32 gamepad app (NOT used by main.c)
│   └── CMakeLists.txt
├── components/
│   ├── km_act/             # Actuator control (DAC for throttle/brake, PWM+DIR for steering)
│   ├── km_coms/            # UART framed protocol (Orin <-> ESP32)
│   ├── km_gpio/            # GPIO/DAC/PWM abstraction
│   ├── km_objects/         # Shared variable store (thread-safe get/set)
│   ├── km_pid/             # PID controller
│   ├── km_rtos/            # FreeRTOS task manager
│   ├── km_sdir/            # AS5600 steering angle sensor (I2C)
│   ├── km_sta/             # State machine
│   └── bluepad32/          # Gamepad library (used by sketch.cpp only)
├── platformio.ini          # Build config
└── sdkconfig.esp32dev      # ESP32 SDK config
```

### Critical Rules

1. **NEVER create a `src/` directory** -- PlatformIO compiles it instead of `main/`
2. **Framework is `espidf`** (NOT arduino)
3. **`src_dir = main`** in platformio.ini tells PIO to use `main/`

## Flashing

```bash
# From the Orin (all hardware is on the Orin)
cd ~/Desktop/kart_medulla
~/.local/bin/pio run --target upload --environment esp32dev --upload-port /dev/ttyUSB0
```

- **Upload baud must be 115200** -- the CP2102 USB-UART bridge fails at higher speeds during flash
- `upload_speed = 115200` is set in `platformio.ini`
- Runtime UART baud is 115200 (binary protocol with Orin)
- If flash hangs at "Connecting...", hold BOOT button, press EN, release BOOT
- After flash, press EN to restart if needed

## Architecture (main.c)

Three FreeRTOS tasks:

| Task | Period | Priority | Function |
|------|--------|----------|----------|
| comms | 10ms (100 Hz) | 2 | UART RX/TX -- receive commands from Orin, send telemetry |
| control | 10ms (100 Hz) | 1 | Read AS5600 sensor, run PID, drive actuators, send steering feedback |
| heartbeat | 1000ms (1 Hz) | 1 | Send heartbeat to Orin |

## Steering Pipeline

1. Orin sends `ORIN_TARG_STEERING` (target angle as float radians via protobuf)
2. `control_task` reads target from `km_objects` store
3. AS5600 sensor read via I2C (400kHz, 5ms timeout) -> actual angle in radians
4. PID computes output (Kp=0.03, Ki=0, Kd=0.0004) -> [-1.0, 1.0]
5. `km_act` drives PWM (magnitude) + DIR pin (sign) on steering motor
6. Actual angle sent back to Orin as `ESP_ACT_STEERING`

**Note:** PID output is negated (`-KM_PID_Calculate(...)`) because motor wiring is reversed. `g_steering_target_received` guard keeps motor off until first steering command from Orin.

## Hardware Pin Map

| Actuator | GPIO | Type | Notes |
|----------|------|------|-------|
| Throttle | 26 | DAC2 | 0-255 output |
| Brake | 25 | DAC1 | 0-255 output |
| Steering PWM | 27 | LEDC PWM | duty 0-255 |
| Steering DIR | 14 | Digital | 1=positive, 0=negative |
| AS5600 SDA | 21 | I2C | 400kHz, addr 0x36 |
| AS5600 SCL | 22 | I2C | |
| LED | 2 | Digital | Onboard LED |

## Safety

- Steering motor limited to **40%** output (`KM_ACT_SetLimit(&dir_act, 0.4)`) for testing
- Increase to 1.0 when system is validated
- `outputLimit` is float 0.0-1.0 (was uint8_t -- caused hardware damage, see errors.md)
- ESP32 watchdog: if no Orin heartbeat received, should apply brakes (TODO -- not yet implemented)

## Debugging

- **Protocol monitor**: `~/.local/bin/pio device monitor -b 115200 -p /dev/ttyUSB0` on Orin
- **ROS2 side**: `ros2 topic echo /esp32/steering` to see feedback from ESP32
- UART0 carries binary protocol only -- ESP-IDF logs are suppressed (`esp_log_level_set("*", ESP_LOG_NONE)`)
- UART2 was removed (GPIO17/GPIO16 reserved for hall sensors on PCB)

## Protocol Details

See `.agents/architecture.md` for full protocol specification including frame format, message types, and protobuf encoding details.
