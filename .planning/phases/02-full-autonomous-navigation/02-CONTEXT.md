# Phase 02: Full Autonomous Navigation - Context

**Gathered:** 2026-03-12
**Status:** Ready for planning

<domain>
## Phase Boundary

Create a new, comprehensive documentation suite in the root project directory. All documentation must be structured in Markdown files.

</domain>

<decisions>
## Implementation Decisions

### Directory Structure
- The documentation should be structured into nested folders by subsystem (e.g., `software`, `hardware`, `assembly`) rather than a flat structure.

### Generation Tool
- The new documentation suite will be purely raw Markdown files (`.md`).
- There will be no site generator (like MkDocs, VitePress, etc.) used for this new suite. Everything should be natively readable directly within the repository (e.g. GitHub UI).

### Content Migration
- **Start Fresh:** Do not directly copy or lightly refactor the files from the `heritage` folder.
- Use the old `heritage` docs purely as an informational reference to write entirely new documentation from scratch.

### LLM Optimization
- Ensure scripts or processes are in place to aggregate the new markdown files into `llms.txt` and `llms-full.txt` files, ensuring AI agents have an optimized way to digest the entire documentation suite at once.

</decisions>

<code_context>
## Existing Code Insights

### Reusable Assets
- The `heritage/kart_docs/generate_llm_files.py` script can likely be used as inspiration or directly adapted to aggregate the new raw markdown suite into `llms.txt` and `llms-full.txt`.

### Established Patterns
- We established a strict "No Emojis" and professional tone in Phase 1 that must be carried forward here when writing the new documentation from scratch.
- The `heritage` folder contains legacy documentation across `kart_docs`, `kart_brain`, and `kart_medulla` to reference.

### Integration Points
- The documentation will live directly in a root `docs/` folder (or similarly named root directory).
- The LLM text generation script can either be run manually or set up as a simple git pre-commit hook/CI job, rather than relying on a MkDocs hook.

</code_context>

<specifics>
## Specific Ideas

- No specific requirements beyond starting fresh and adhering to the structural and tool decisions listed above.

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope

</deferred>

---

*Phase: 02-full-autonomous-navigation*
*Context gathered: 2026-03-12*