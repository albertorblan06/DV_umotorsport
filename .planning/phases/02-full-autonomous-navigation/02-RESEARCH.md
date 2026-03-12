# Phase 02: Full Autonomous Navigation - Research

**Researched:** 2026-03-12
**Domain:** Documentation Architecture & AI-Optimized Markdown
**Confidence:** HIGH

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions

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

### Claude's Discretion

### Reusable Assets
- The `heritage/kart_docs/generate_llm_files.py` script can likely be used as inspiration or directly adapted to aggregate the new raw markdown suite into `llms.txt` and `llms-full.txt`.

### Established Patterns
- We established a strict "No Emojis" and professional tone in Phase 1 that must be carried forward here when writing the new documentation from scratch.
- The `heritage` folder contains legacy documentation across `kart_docs`, `kart_brain`, and `kart_medulla` to reference.

### Integration Points
- The documentation will live directly in a root `docs/` folder (or similarly named root directory).
- The LLM text generation script can either be run manually or set up as a simple git pre-commit hook/CI job, rather than relying on a MkDocs hook.

### Deferred Ideas (OUT OF SCOPE)
None — discussion stayed within phase scope
</user_constraints>

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|-----------------|
| AUTO-01 | Kart can autonomously navigate a track defined by traffic cones. | The documentation suite will cover the algorithms and nodes responsible for this navigation (e.g., ROS 2 pure pursuit, Delaunay triangulation for track limits). |
| AUTO-03 | System detects when the track is completed. | The documentation suite will outline the lap completion logic (e.g., start/finish line detection, SLAM loop closure, or distance heuristics). |
</phase_requirements>

## Standard Stack

### Core
| Library / Tool | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| Markdown | N/A | Documentation formatting | Universally supported by GitHub/GitLab, highly readable raw text format. |
| Python | 3.10+ | Scripting `llms.txt` generation | Robust standard library (`os`, `pathlib`, `re`) for parsing and concatenating text files. |

## Architecture Patterns

### Recommended Project Structure
```
docs/
├── hardware/        # Actuators, ESP32 wiring, sensors (ZED camera)
├── software/        # ROS 2 nodes, perception pipeline (YOLOv11), planner
├── assembly/        # Mechanical constraints, mounting instructions
└── integration/     # End-to-end full autonomous navigation tests
scripts/
└── generate_llms_txt.py # Script to aggregate markdown into llms.txt and llms-full.txt
```

### Anti-Patterns to Avoid
- **Site Generators:** Do not introduce MkDocs, Sphinx, or VitePress.
- **Emojis:** Do not use emojis in any documentation files. Keep a professional tone.
- **Copy-Pasting Legacy:** Do not copy the `heritage` folder contents directly. Rewrite them.

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| AI Documentation Aggregation | A complex AST parser | `pathlib` tree traversal concatenating `.md` files | A simple Python script is faster, easier to maintain, and exactly fulfills the `llms.txt` requirement. |

## Common Pitfalls

### Pitfall 1: Broken Internal Links
**What goes wrong:** Markdown files link to each other using absolute paths or incorrect relative paths.
**Why it happens:** Moving files into a nested directory structure without updating links.
**How to avoid:** Use standard relative paths (e.g., `../software/planner.md`) and verify links in the GitHub UI.

### Pitfall 2: Overly Complex Aggregation Script
**What goes wrong:** The `llms.txt` generation script becomes brittle and crashes on new folders.
**Why it happens:** Hardcoding specific folder names instead of dynamically walking the `docs/` directory.
**How to avoid:** Use `os.walk` or `pathlib.Path.rglob('*.md')` to dynamically discover all markdown files.

## Code Examples

Verified patterns from official sources:

### Python LLM Aggregation Snippet (Inspiration)
```python
import os
from pathlib import Path

def generate_llm_txt(docs_dir="docs", output_file="llms.txt"):
    docs_path = Path(docs_dir)
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write("# Full Project Documentation\n\n")
        for md_file in sorted(docs_path.rglob("*.md")):
            outfile.write(f"## File: {md_file.relative_to(docs_path)}\n\n")
            outfile.write(md_file.read_text(encoding='utf-8'))
            outfile.write("\n\n---\n\n")
```

## Validation Architecture

> Skip this section entirely if workflow.nyquist_validation is explicitly set to false in .planning/config.json. If the key is absent, treat as enabled.

### Test Framework
| Property | Value |
|----------|-------|
| Framework | Python `unittest` or `pytest` (for the script) |
| Config file | none |
| Quick run command | `python3 scripts/generate_llms_txt.py` |
| Full suite command | `python3 scripts/generate_llms_txt.py && cat llms.txt | wc -l` |

### Phase Requirements → Test Map
| Req ID | Behavior | Test Type | Automated Command | File Exists? |
|--------|----------|-----------|-------------------|-------------|
| AUTO-01 | Documentation covers autonomous navigation | integration | `grep -i "autonomous" llms.txt` | ❌ Wave 0 |
| AUTO-03 | Documentation covers track completion | integration | `grep -i "track" llms.txt` | ❌ Wave 0 |

### Sampling Rate
- **Per task commit:** Generate `llms.txt` to verify the script works.
- **Per wave merge:** Manual review of the generated markdown files.
- **Phase gate:** Ensure `llms.txt` and `llms-full.txt` are populated with all docs content.

### Wave 0 Gaps
- [ ] `scripts/generate_llms_txt.py` — Needed to aggregate the markdown files.

## Sources

### Primary (HIGH confidence)
- User Constraints (from `02-CONTEXT.md`) - Strict guidance on Markdown documentation, directory structures, and avoiding site generators.
- Project Requirements (`REQUIREMENTS.md`) - Defines the autonomous navigation topics to be documented.

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH - Core Python and Markdown are standard.
- Architecture: HIGH - Dictated by `02-CONTEXT.md`.
- Pitfalls: HIGH - Known issues with Markdown links and script traversal.

**Research date:** 2026-03-12
**Valid until:** 2026-04-12
