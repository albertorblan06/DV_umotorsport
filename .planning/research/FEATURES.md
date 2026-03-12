# Feature Research

**Domain:** Autonomous Vehicle Software Engineering (Testing, Refactoring, Scrum)
**Researched:** 2026-03-12
**Confidence:** HIGH

## Feature Landscape

### Table Stakes (Users Expect These)

Features expected for a robust engineering culture in a mixed ROS 2 / ESP32 project. Missing these means the "v2.0 Full Remake" goals won't be met.

| Feature | Why Expected | Complexity | Notes |
|---------|--------------|------------|-------|
| **ROS 2 GTest/PyTest Integration** | Standard for ROS 2 unit testing (`colcon test`). Essential for validating planning/vision logic. | MEDIUM | Relies on mocking hardware interfaces. |
| **ESP32 Unity Unit Testing** | Standard for embedded firmware. Required to test PID and comms logic without the physical kart. | MEDIUM | Can be run natively (Software-in-the-Loop) or on target. |
| **Automated CI/CD Pipeline** | Code must be proven to compile and pass tests on every PR to prevent regressions. | MEDIUM | GitHub Actions or GitLab CI. Requires a Dockerized ROS 2 Humble environment. |
| **Static Code Analysis** | Enforces clean code and catches memory/concurrency bugs early. | LOW | `clang-tidy`, `cppcheck`, and `ament_lint`. |
| **Scrum Artifacts & Rituals** | Backlog, sprint boards, and documented iterations are required for the March 25th deadline. | LOW | GitHub Projects/Issues. Keep it lightweight. |

### Differentiators (Competitive Advantage)

Features that set the engineering pipeline apart, specifically addressing the low Big O and hardware constraints.

| Feature | Value Proposition | Complexity | Notes |
|---------|-------------------|------------|-------|
| **Big O / Performance Benchmarking in CI** | Ensures refactoring actually improves algorithmic complexity and maintains 100Hz real-time latency. | HIGH | Use Google Benchmark. Fail CI if latency exceeds 10ms (100Hz requirement). |
| **Hardware-in-the-Loop (HIL) Testing** | Validates ESP32 firmware on actual silicon, catching timing and hardware-specific issues. | HIGH | Requires a dedicated ESP32 connected to a CI runner, stubbing UART inputs. |
| **Automated ROS Bag Regression Tests** | Validates computer vision and trajectory planning against known good real-world sensor data. | HIGH | CI replays ROS bags and checks if the output trajectory matches expectations. |

### Anti-Features (Commonly Requested, Often Problematic)

Features that seem good but create problems in a robotics context.

| Feature | Why Requested | Why Problematic | Alternative |
|---------|---------------|-----------------|-------------|
| **100% Code Coverage** | Sounds like the ultimate quality guarantee. | Impossible/brittle for hardware abstraction layers and I/O. Leads to useless assertion tests. | Target 80% coverage on core logic (planning, math, PID); mock I/O. |
| **Full Kart Test per PR** | "We should test on the real thing." | Dangerous, requires physical space, slow, blocks development. | Rely on Gazebo simulation tests + HIL for PRs; physical kart for Release candidates. |
| **Heavy Enterprise Scrum** | "We need strict Agile." | Daily hour-long standups and story pointing drag down a fast-moving robotics team. | Lightweight Scrum: 2-week sprints, async standups, GitHub Projects. |

## Feature Dependencies

```
[ROS 2 Docker Environment]
    └──requires──> [CI/CD Pipeline]
                       └──requires──> [Automated ROS Bag Tests]
                       └──requires──> [Performance Benchmarking]

[ESP32 Unity Tests]
    └──requires──> [Hardware-in-the-loop (HIL) Runner]

[Refactoring for Low Big O]
    └──requires──> [ROS 2 GTest] (To ensure no regressions)
    └──requires──> [Performance Benchmarking] (To prove it worked)
```

### Dependency Notes

- **[CI/CD Pipeline] requires [ROS 2 Docker Environment]:** Compiling ROS 2 and running tests requires a consistent, isolated OS environment (Ubuntu 22.04 / Humble).
- **[Refactoring] requires [ROS 2 GTest]:** You cannot safely refactor the Jetson planning algorithms for better Big O without unit tests proving the logic still works.
- **[HIL Runner] requires [ESP32 Unity Tests]:** The testing framework must be established before it can be deployed to the physical hardware runner.

## MVP Definition

### Launch With (v1 - Core Infrastructure)

Minimum viable infrastructure to begin the refactoring process safely.

- [x] **ROS 2 GTest & ESP32 Unity** — Needed to write tests before refactoring.
- [x] **CI/CD Pipeline (Build + Test)** — Needed to enforce tests pass on PR.
- [x] **Lightweight Scrum Board** — Needed to track the refactoring backlog.
- [x] **Static Analysis** — Enforces clean code immediately.

### Add After Validation (v1.x - Advanced Testing)

Features to add once core tests are written.

- [ ] **Performance Benchmarking** — To prove the Big O refactoring was successful.
- [ ] **Automated ROS Bag Tests** — To validate the CV pipeline holistically.

### Future Consideration (v2+ - Hardware CI)

Features to defer until the software refactoring is complete.

- [ ] **Hardware-in-the-Loop (HIL)** — High setup cost, defer until basic SIL (Software-in-the-loop) is solid.

## Feature Prioritization Matrix

| Feature | User Value | Implementation Cost | Priority |
|---------|------------|---------------------|----------|
| ROS 2 GTest / ESP32 Unity | HIGH | MEDIUM | P1 |
| CI/CD Pipeline | HIGH | LOW | P1 |
| Scrum Artifacts | HIGH | LOW | P1 |
| Static Code Analysis | MEDIUM | LOW | P1 |
| Performance Benchmarking | HIGH | MEDIUM | P2 |
| ROS Bag Regression | HIGH | HIGH | P2 |
| HIL Testing | MEDIUM | HIGH | P3 |

**Priority key:**
- P1: Must have for launch
- P2: Should have, add when possible
- P3: Nice to have, future consideration

## Competitor Feature Analysis

| Feature | Typical Academic Team | Professional Autonomous Racing | Our Approach (v2.0) |
|---------|-----------------------|--------------------------------|---------------------|
| **Testing** | Manual testing on track | HIL, SIL, full simulation CI | SIL (GTest/Unity) + Simulation CI |
| **Process** | Ad-hoc, chaos | Strict Agile, code review | Lightweight Scrum, PR reviews |
| **Performance**| "If it runs, it runs" | Profiling, strict latency budgets | Big O refactoring + Benchmarking |

## Sources

- `.planning/PROJECT.md`
- ROS 2 Humble Testing Documentation (GTest/Ament)
- PlatformIO & Unity Embedded Testing Standards
- Agile/Scrum best practices for robotics teams

---
*Feature research for: Testing, Refactoring, and Scrum (Autonomous Kart)*
*Researched: 2026-03-12*