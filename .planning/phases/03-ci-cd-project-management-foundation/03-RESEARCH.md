<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions
- CI pipeline triggers only on Pull Requests (to save runner minutes while protecting main).
- Strict Failure: The CI build must fail immediately if any linting or formatting rule is violated (clang-tidy, Ruff).
- Standard Kanban columns: Todo, In Progress, Review, Done. Use standard GitHub Projects integration.
- Full Compilation: The CI must actually set up the environments (ROS 2 / ESP-IDF) and compile the code, not just run static analysis.

### Claude's Discretion
- Exact configuration of Ruff and clang-tidy rules (assuming standard modern C++/Python best practices).
- Specific base images for the ROS 2 (Humble) and ESP-IDF containers in GitHub Actions.

### Deferred Ideas (OUT OF SCOPE)
- Unit test execution within CI (This belongs to Phase 5).
- Hardware-in-the-Loop (HIL) testing within CI (This belongs to Phase 6).
</user_constraints>

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|-----------------|
| SCRU-01 | Project backlog and iterations are tracked via lightweight GitHub Projects boards | GitHub Projects API/CLI usage pattern |
| METR-01 | PR CI pipeline executes automated tests and linters | GitHub Actions workflow config and job dependencies |
| METR-02 | Static code analysis (clang-tidy, Ruff) fails CI on violations | Linter configurations (`pyproject.toml`, `.clang-tidy`) with strict failure flags |
</phase_requirements>

# Phase 3: CI/CD & Project Management Foundation - Research

**Researched:** 2026-03-12
**Domain:** GitHub Actions, Project Boards, Static Analysis
**Confidence:** HIGH

## Summary

This phase establishes the foundational tools for development hygiene and project tracking. The CI pipeline will strictly enforce code quality (via Ruff for Python and clang-tidy for C++) and guarantee that all code compiles fully within official ROS 2 and ESP-IDF environments on every Pull Request. Additionally, a standard Kanban GitHub Project board will be created to manage sprints.

**Primary recommendation:** Use matrix builds or separate jobs in a single GitHub Actions workflow (`.github/workflows/ci.yml`) targeting `ros:humble-ros-base` and `espressif/idf:v5.3` images to isolate the environments, while applying strict lint configurations locally.

## Standard Stack

### Core
| Library / Tool | Version | Purpose | Why Standard |
|----------------|---------|---------|--------------|
| GitHub Actions | v4 | Automated CI pipeline | Native, zero-setup platform for GitHub repositories |
| GitHub Projects | v2 | Scrum Kanban board | Seamless integration with issues and PRs |
| Ruff | Latest | Python static analysis | Orders of magnitude faster than Flake8/Black, highly configurable |
| clang-tidy | >=14.0 | C++ static analysis | Industry standard for modern C++ guidelines (Core, CERT, MISRA) |

### Supporting
| Library / Image | Version | Purpose | When to Use |
|-----------------|---------|---------|-------------|
| `ros:humble-ros-base` | Humble | ROS 2 build container | Minimal OS with ROS 2 core packages for compiling Orin nodes |
| `espressif/idf` | v5.3 / v5.5 | ESP32 build container | Official pre-configured ESP-IDF toolchain for compilation |

### Alternatives Considered
| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| Ruff | Flake8 + Black | Flake8+Black requires multiple tools and is slower. Ruff is the modern standard. |
| GitHub Actions | Jenkins | Jenkins requires hosting and maintenance, while GH Actions is native and free. |

## Architecture Patterns

### Recommended Project Structure
```text
.github/
└── workflows/
    └── ci.yml            # Main PR pipeline
.clang-tidy               # Global C++ linting rules
pyproject.toml            # Global Python/Ruff config
```

### Pattern 1: Multi-Container Workflow
**What:** Separate the build environments using job-level `container` directives.
**When to use:** When a single repository contains multiple distinct tech stacks (ROS 2 and ESP-IDF).
**Example:**
```yaml
jobs:
  ros2-build:
    runs-on: ubuntu-22.04
    container: ros:humble-ros-base
    steps:
      - uses: actions/checkout@v4
      - run: colcon build --cmake-args -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
  
  esp32-build:
    runs-on: ubuntu-22.04
    container: espressif/idf:release-v5.3
    steps:
      - uses: actions/checkout@v4
      - run: idf.py build
```

### Anti-Patterns to Avoid
- **Anti-pattern:** Compiling on the host `ubuntu-latest` and manually installing ROS 2/ESP-IDF dependencies.
  - *Why it's bad:* Extremely slow pipeline due to downloading gigabytes of apt packages on every run.
  - *What to do instead:* Use the official pre-built Docker containers (`ros:humble...` and `espressif/idf...`).

## Common Pitfalls

### Pitfall 1: C++ Linting Fails to Find Headers (compile_commands.json)
**What goes wrong:** `clang-tidy` throws massive errors complaining about missing standard headers or missing ROS/ESP macros.
**Why it happens:** It lacks the exact compilation flags used during the build.
**How to avoid:** Generate `compile_commands.json` during the build step. For CMake/ROS2: `colcon build --cmake-args -DCMAKE_EXPORT_COMPILE_COMMANDS=ON`. For ESP-IDF: it automatically generates it in the `build/` folder. Feed this to clang-tidy using `-p build/`.

### Pitfall 2: CI Trigger Spam
**What goes wrong:** Runner minutes are depleted because CI triggers on every commit to main or every branch push.
**Why it happens:** Missing or broad `on:` triggers.
**How to avoid:** Explicitly constrain the trigger as requested in decisions:
```yaml
on:
  pull_request:
    branches: [ main ]
```

## Code Examples

### Standard Ruff Configuration (`pyproject.toml`)
```toml
[tool.ruff]
line-length = 100
target-version = "py310"

[tool.ruff.lint]
select = [
    "E",  # pycodestyle errors
    "W",  # pycodestyle warnings
    "F",  # pyflakes
    "I",  # isort
    "C",  # flake8-comprehensions
    "B",  # flake8-bugbear
]
ignore = []
```

### Standard clang-tidy Configuration (`.clang-tidy`)
```yaml
Checks: >
  -*,
  bugprone-*,
  cppcoreguidelines-*,
  modernize-*,
  performance-*,
  readability-*
WarningsAsErrors: '*'
```
*Note: `WarningsAsErrors: '*'` enforces strict failure.*

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| Flake8 + Black + isort | Ruff | 2023 | 10-100x faster, single dependency for all Python formatting/linting |
| cpplint | clang-tidy | ~2018 | AST-based linting is significantly more powerful than regex-based linting |

## Validation Architecture

### Test Framework
| Property | Value |
|----------|-------|
| Framework | GitHub Actions (CI) |
| Config file | `.github/workflows/ci.yml` |
| Quick run command | `gh workflow run ci.yml` |
| Full suite command | (Trigger via PR creation) |

### Phase Requirements → Test Map
| Req ID | Behavior | Test Type | Automated Command | File Exists? |
|--------|----------|-----------|-------------------|-------------|
| SCRU-01 | Board exists with correct columns | Manual | Check UI/CLI | ❌ Wave 0 |
| METR-01 | Pipeline runs on PRs | Integration | `gh run list --workflow=ci.yml` | ❌ Wave 0 |
| METR-02 | Fails on lint errors | Unit/CI | Add bad code and verify CI failure | ❌ Wave 0 |

### Sampling Rate
- **Per task commit:** Local `ruff check .` or `clang-tidy`
- **Per wave merge:** Wait for PR GitHub Actions status to turn green
- **Phase gate:** PRs are successfully blocked from merging if pipeline fails.

### Wave 0 Gaps
- [ ] `.github/workflows/ci.yml`
- [ ] `pyproject.toml`
- [ ] `.clang-tidy`
- [ ] Initial project board setup

## Sources

### Primary (HIGH confidence)
- Official GitHub Actions Documentation (Syntax and Triggers)
- Ruff Official Documentation (Astral)
- ESP-IDF Docker Images (espressif/idf DockerHub)
- ROS 2 Humble Docker Images (osrf/ros DockerHub)

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH - Directly follows modern C++/Python and GH Actions best practices.
- Architecture: HIGH - Docker containers for complex C++ toolchains in CI is standard.
- Pitfalls: HIGH - `compile_commands.json` is notoriously the biggest hurdle for C++ linting.

**Research date:** 2026-03-12
**Valid until:** 2026-09-12