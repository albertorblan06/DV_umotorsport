---
phase: 02
slug: full-autonomous-navigation
status: draft
nyquist_compliant: false
wave_0_complete: false
created: 2026-03-12
---

# Phase 02 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | markdownlint / script execution |
| **Config file** | none — Wave 0 installs |
| **Quick run command** | `markdownlint docs/` |
| **Full suite command** | `python scripts/compile_llms.py` |
| **Estimated runtime** | ~5 seconds |

---

## Sampling Rate

- **After every task commit:** Run `markdownlint docs/`
- **After every plan wave:** Run `python scripts/compile_llms.py`
- **Before `/gsd-verify-work`:** Full suite must be green
- **Max feedback latency:** 5 seconds

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|-----------|-------------------|-------------|--------|
| 02-01-01 | 01 | 1 | AUTO-01 | format | `markdownlint docs/software/planner.md` | ❌ W0 | ⬜ pending |
| 02-01-02 | 01 | 1 | AUTO-03 | format | `markdownlint docs/software/control.md` | ❌ W0 | ⬜ pending |
| 02-02-01 | 02 | 2 | AUTO-01 | format | `python scripts/compile_llms.py` | ❌ W0 | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*

---

## Wave 0 Requirements

- [ ] `docs/software/planner.md` — stubs for AUTO-01
- [ ] `docs/software/control.md` — stubs for AUTO-03
- [ ] `scripts/compile_llms.py` — python script to aggregate

*If none: "Existing infrastructure covers all phase requirements."*

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| Documentation review | AUTO-01 | Human reading required | Read generated llms.txt |

*If none: "All phase behaviors have automated verification."*

---

## Validation Sign-Off

- [ ] All tasks have `<automated>` verify or Wave 0 dependencies
- [ ] Sampling continuity: no 3 consecutive tasks without automated verify
- [ ] Wave 0 covers all MISSING references
- [ ] No watch-mode flags
- [ ] Feedback latency < 5s
- [ ] `nyquist_compliant: true` set in frontmatter

**Approval:** pending
