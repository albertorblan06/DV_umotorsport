# Phase 3: CI/CD & Project Management Foundation - Context

**Gathered:** 2026-03-12
**Status:** Ready for planning

<domain>
## Phase Boundary

Establishing GitHub Actions CI pipelines (linting/tests) and GitHub Projects Scrum boards. The development workflow enforces clean code and tracks progress automatically.

</domain>

<decisions>
## Implementation Decisions

### CI Scope & Triggers
- CI pipeline triggers only on Pull Requests (to save runner minutes while protecting main).

### Linting Strictness
- Strict Failure: The CI build must fail immediately if any linting or formatting rule is violated (clang-tidy, Ruff).

### Scrum Board Structure
- Standard Kanban columns: Todo, In Progress, Review, Done. Use standard GitHub Projects integration.

### Build Context
- Full Compilation: The CI must actually set up the environments (ROS 2 / ESP-IDF) and compile the code, not just run static analysis.

### Claude's Discretion
- Exact configuration of Ruff and clang-tidy rules (assuming standard modern C++/Python best practices).
- Specific base images for the ROS 2 (Humble) and ESP-IDF containers in GitHub Actions.

</decisions>

<code_context>
## Existing Code Insights

### Reusable Assets
- None specifically for CI/CD yet. No `.github/workflows/` directory exists.
- The project appears to have Python and C++ components (Orin/ROS 2 and ESP32).

### Established Patterns
- Clean code and strict engineering standards are the goal for Milestone v2.0.

### Integration Points
- `.github/workflows/ci.yml` will be the primary integration point.
- The ROS 2 colcon workspace and ESP-IDF CMake/PlatformIO build commands will need to be executed inside the CI jobs.

</code_context>

<specifics>
## Specific Ideas

- The CI must fully compile both the ROS 2 workspace (for the Orin) and the ESP32 firmware to verify build integrity on PRs.

</specifics>

<deferred>
## Deferred Ideas

- Unit test execution within CI (This belongs to Phase 5).
- Hardware-in-the-Loop (HIL) testing within CI (This belongs to Phase 6).

</deferred>

---

*Phase: 03-ci-cd-project-management-foundation*
*Context gathered: 2026-03-12*
