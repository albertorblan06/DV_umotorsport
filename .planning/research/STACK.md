# Technology Stack

**Project:** DV_umotorsport (Milestone: v2.0 Full Remake)
**Researched:** 2026-03-12

## Recommended Stack Additions

### Unit Testing & Mocking (ROS 2 / Orin)
| Technology | Version | Purpose | Why |
|------------|---------|---------|-----|
| **GTest / GMock** | v1.14+ | C++ Unit Testing | Native integration with `ament_cmake_gtest` in ROS 2 Humble. Industry standard for C++. |
| **pytest** | 8.x | Python Unit Testing | Standard for ROS 2 Python nodes. Integrates with `ament_cmake_pytest`. |
| **Google Benchmark**| v1.8+ | Algorithmic Complexity | Specifically to prove Big O metrics. Features `SetComplexityN` to automatically calculate asymptotic complexity (O(N), O(N^2), etc.) empirically. |

### Unit Testing (ESP32 / Firmware)
| Technology | Version | Purpose | Why |
|------------|---------|---------|-----|
| **Unity** | 2.5+ | C/C++ Firmware Testing | Native to ESP-IDF framework. Extremely lightweight, perfect for FreeRTOS tasks and hardware mocking. |
| **CMock** | Latest | Hardware Mocking | Pairs with Unity to mock ESP32 hardware peripherals (DAC, PWM, UART) without needing the physical board for pure logic tests. |

### Clean Code & Static Analysis
| Technology | Version | Purpose | Why |
|------------|---------|---------|-----|
| **clang-tidy** | 14+ | C++ Linter/Analyzer | Enforces Modern C++ standards, finds memory leaks, and ensures clean code. Easily integrates into `ament_cmake`. |
| **cppcheck** | 2.10+ | Static Analysis | Fast, checks for undefined behavior and dangerous patterns in C/C++ firmware and ROS nodes. |
| **Ruff** | 0.x | Python Linter | Blazing fast replacement for flake8/pylint. Enforces strict Python standards for perception/planning nodes. |
| **lcov / gcov** | Latest | Code Coverage | Generates HTML reports to ensure all critical control paths (fail-safes) are tested. |

### Scrum & Project Management
| Technology | Version | Purpose | Why |
|------------|---------|---------|-----|
| **GitHub Projects** | V2 | Scrum Tracking | Tightly couples with PRs and issues. Low friction, avoiding the overhead of Jira while supporting Sprints, velocity, and story points. |

## Alternatives Considered

| Category | Recommended | Alternative | Why Not |
|----------|-------------|-------------|---------|
| Complexity Profiling | Google Benchmark | Valgrind/Callgrind | Callgrind is great for overall profiling, but Google Benchmark has built-in mathematical curve fitting to explicitly prove Big O requirements. |
| Scrum Tracking | GitHub Projects | Jira | Jira is too heavy for a university/small team project and disconnects the code from the sprint board. |
| Python Linting | Ruff | Pylint + Flake8 | Ruff replaces both, runs in milliseconds, and has better modern defaults. |

## Installation & Integration

```bash
# ROS 2 Testing Dependencies (Ubuntu)
sudo apt install ros-humble-ament-cmake-gtest ros-humble-ament-cmake-pytest
sudo apt install clang-tidy cppcheck lcov
pip install ruff pytest

# Google Benchmark (for Big O validation)
git clone https://github.com/google/benchmark.git
cd benchmark && cmake -E make_directory "build"
cmake -E chdir "build" cmake -DBENCHMARK_DOWNLOAD_DEPENDENCIES=on -DCMAKE_BUILD_TYPE=Release ../
cmake --build "build" --config Release
sudo cmake --build "build" --config Release --target install
```

## Anti-Patterns to Avoid

- **Do NOT** use heavy end-to-end simulation tests to prove algorithmic complexity. Use isolated `Google Benchmark` microbenchmarks on pure functions.
- **Do NOT** test hardware peripherals directly in unit tests. Use `CMock` to mock the UART/PWM interfaces so the PID logic can be tested on standard CI runners.
- **Do NOT** add heavy Agile/Scrum tools like Jira. Keep iterations documented directly in GitHub using Sprint boards and Markdown files.

## Sources

- [ROS 2 Humble Testing Documentation](https://docs.ros.org/en/humble/Tutorials/Intermediate/Testing/Testing-Main.html) (HIGH confidence)
- [Google Benchmark GitHub](https://github.com/google/benchmark) (HIGH confidence)
- [ESP-IDF Unit Testing with Unity](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/unit-tests.html) (HIGH confidence)