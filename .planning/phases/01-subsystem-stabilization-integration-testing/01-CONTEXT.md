# Phase 1: Subsystem Stabilization & Integration Testing - Context

**Gathered:** 2026-03-12
**Status:** Ready for planning

<domain>
## Phase Boundary

Ensure perception, actuation, and communication systems are robust and reliable independently and in simulation before full autonomy. The first step of this project is to reorganize and remake documentation methodically in markdown files.

</domain>

<decisions>
## Implementation Decisions

### Documentation Structure
- Use the existing `kart_docs` MkDocs structure but reorganize and expand it methodically.
- Content must be written in professional, concise Markdown, adhering strictly to the "no emojis" rule.
- Ensure clear separation between hardware assembly instructions, software architecture/deployment, and agent/developer workflows (`.agents/`).

### Organization Criteria
- Structure by logical subsystems: Hardware (Assembly, Powertrain, Steering, Electronics, Sensors) vs Software (Architecture, ROS 2 nodes, ESP32 firmware).
- Keep BOM (Bill of Materials), tools, and FAQ separated but easily accessible.
- Maintain legacy iterations under a dedicated `iterations/` folder.

### Integration with Existing Docs
- Update `mkdocs.yml` navigation structure to match the newly reorganized files.
- Move agent-specific workflow docs out of `kart_docs/` into `.agents/` if they accidentally got mixed. Official docs stay in `kart_docs/`.

### Claude's Discretion
- Specific folder nesting depths for minor components.
- Naming conventions for new markdown files (e.g., lowercase with hyphens).

</decisions>

<code_context>
## Existing Code Insights

### Reusable Assets
- `kart_docs/mkdocs.yml`: Existing configuration to be updated.
- `.agents/methodology.md`: Contains the strict rules for documentation (no emojis, professional tone).

### Established Patterns
- MkDocs Material theme is used. Admonitions, details, and superfences are enabled.
- The `.agents/` directory is exclusively for developer/AI reference, whereas `kart_docs/` is the official public-facing project documentation.

### Integration Points
- Documentation builds via `uv run mkdocs serve` locally and deploys to GitHub Pages.
- CI/CD hooks in `mkdocs.yml` (`generate_llm_hook.py`, `generate_bom_hook.py`) should be preserved.

</code_context>

<specifics>
## Specific Ideas

- "I want all the documentation metodolically organized in md files"
- Ensure that agent-oriented files stay strictly in `.agents/` while public project files stay in `kart_docs/`.

</specifics>

<deferred>
## Deferred Ideas

- None — discussion stayed within phase scope.
</deferred>

---

*Phase: 01-subsystem-stabilization-integration-testing*
*Context gathered: 2026-03-12*