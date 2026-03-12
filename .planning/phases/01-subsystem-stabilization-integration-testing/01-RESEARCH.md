# Phase 01: Subsystem Stabilization & Integration Testing - Research

**Researched:** 2026-03-12
**Domain:** Documentation Architecture & Subsystem Integration
**Confidence:** HIGH

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions
- Use the existing `kart_docs` MkDocs structure but reorganize and expand it methodically.
- Content must be written in professional, concise Markdown, adhering strictly to the "no emojis" rule.
- Ensure clear separation between hardware assembly instructions, software architecture/deployment, and agent/developer workflows (`.agents/`).
- Structure by logical subsystems: Hardware (Assembly, Powertrain, Steering, Electronics, Sensors) vs Software (Architecture, ROS 2 nodes, ESP32 firmware).
- Keep BOM (Bill of Materials), tools, and FAQ separated but easily accessible.
- Maintain legacy iterations under a dedicated `iterations/` folder.
- Update `mkdocs.yml` navigation structure to match the newly reorganized files.
- Move agent-specific workflow docs out of `kart_docs/` into `.agents/` if they accidentally got mixed. Official docs stay in `kart_docs/`.

### Claude's Discretion
- Specific folder nesting depths for minor components.
- Naming conventions for new markdown files (e.g., lowercase with hyphens).

### Deferred Ideas (OUT OF SCOPE)
- None — discussion stayed within phase scope.
</user_constraints>

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|-----------------|
| AUTO-02 | Planner generates feasible racing lines based on localized cones. | Map planner to Software/Architecture docs. |
| PERC-01 | Detects track boundaries/cones at >= 15Hz using YOLOv11 and ZED. | Sensor docs and ROS 2 nodes structure. |
| PERC-02 | Converts bounding boxes and depth to 3D local coordinates. | Computer vision pipeline documentation. |
| CTRL-01 | ESP32 outputs PWM to steering with accurate AS5600 feedback. | Hardware/Steering and Firmware docs. |
| CTRL-02 | ESP32 drives Throttle and Brake DACs reliably. | Powertrain and Firmware docs. |
| CTRL-03 | ESP32 heartbeat failure leads to safe state (brakes applied). | Hardware/Electronics and safety docs. |
| TELE-01 | ROS 2 dashboard displays current state, speeds, and camera feeds. | Software/ROS 2 nodes and Architecture docs. |
</phase_requirements>

## Summary

The initial focus of Phase 1 is a methodical reorganization of the project's documentation using MkDocs, establishing a solid foundation before hardware/software integration testing. The structure mandates a clear separation between public-facing project docs (`kart_docs/`) and AI/developer workflow docs (`.agents/`). The documentation must comprehensively cover both Hardware (subdivided into Assembly, Powertrain, Steering, Electronics, Sensors) and Software (Architecture, ROS 2 nodes, ESP32 firmware) to support the underlying stabilization and integration of the Kart's subsystems.

**Primary recommendation:** Build out the `kart_docs/` directory structure with lowercase-hyphenated Markdown files, update `mkdocs.yml` to reflect the new hierarchy, and ensure all agent-related methodology is isolated in `.agents/`.

## Standard Stack

### Core
| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| MkDocs | Latest | Static site generation | Existing project standard for `kart_docs` |
| mkdocs-material | Latest | Theme for MkDocs | Established pattern in project |

## Architecture Patterns

### Recommended Project Structure
```
.agents/
├── methodology.md        # Agent rules and professional guidelines
└── workflows/            # Any AI/developer specific processes

kart_docs/
├── mkdocs.yml            # Updated navigation
├── docs/
│   ├── hardware/
│   │   ├── assembly/
│   │   ├── powertrain/
│   │   ├── steering/
│   │   ├── electronics/
│   │   └── sensors/
│   ├── software/
│   │   ├── architecture/
│   │   ├── ros2-nodes/
│   │   └── esp32-firmware/
│   ├── resources/
│   │   ├── bom.md
│   │   ├── tools.md
│   │   └── faq.md
│   └── iterations/       # Legacy builds
```

### Anti-Patterns to Avoid
- **Mixing audiences:** Storing agent instructions in `kart_docs/` or user docs in `.agents/`.
- **Informal language:** Using emojis or unprofessional language in official documentation.

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| CI/CD generation | Custom scripts for BOM | Existing `generate_bom_hook.py` | Already integrated in `mkdocs.yml` |

## Common Pitfalls

### Pitfall 1: Broken MkDocs Navigation
**What goes wrong:** `mkdocs serve` fails or shows empty sections.
**Why it happens:** Files are moved but `mkdocs.yml` `nav` section is not updated to match the new paths.
**How to avoid:** Always update `mkdocs.yml` in the same commit as moving or creating `.md` files.

### Pitfall 2: Emojis in Markdown
**What goes wrong:** Validation fails against `.agents/methodology.md` rules.
**Why it happens:** Default LLM behavior often includes emojis.
**How to avoid:** Explicit prompt instructions to strip all emojis during markdown generation.

## Validation Architecture

### Test Framework
| Property | Value |
|----------|-------|
| Framework | MkDocs |
| Config file | `kart_docs/mkdocs.yml` |
| Quick run command | `uv run mkdocs build --strict` |
| Full suite command | `uv run mkdocs build --strict` |

### Phase Requirements → Test Map
| Req ID | Behavior | Test Type | Automated Command | File Exists? |
|--------|----------|-----------|-------------------|-------------|
| DOCS-01 | MkDocs builds without broken links | integration | `uv run mkdocs build --strict` | ✅ Wave 0 |

### Wave 0 Gaps
- [ ] `kart_docs/mkdocs.yml` requires structural update.

## Sources

### Primary (HIGH confidence)
- User CONTEXT.md definitions for documentation structure.
- STATE.md indicating transition to phase 1.

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH - Dictated by context and existing repo state.
- Architecture: HIGH - Dictated explicitly by context requirements.
- Pitfalls: HIGH - Based on MkDocs standard behaviors.

**Research date:** 2026-03-12
**Valid until:** 2026-04-12
