# Agent Errors and Lessons Learned

Every agent session must record failed assumptions, errors, or bugs introduced to this file. Before starting a new session, review this document to avoid repeating past mistakes.

## Format
- **Date/Session:** [Insert Date]
- **Context:** [What the agent was trying to achieve]
- **The Error:** [What went wrong, stack trace, failed command, or bug]
- **The Resolution/Lesson:** [How it was fixed and what the agent must do in the future]

---

## Error Log

- **Date/Session:** 2026-03-11
- **Context:** Setting up the initial repository structure.
- **The Error:** Cloned the `kart_docs` repository directly into the `umotorsport` root folder instead of inside its own subdirectory (`umotorsport/kart_docs`), mixing files.
- **The Resolution/Lesson:** Used `bash` to properly move all `kart_docs` files into a dedicated subdirectory. In the future, always verify the target directory path when running `git clone` or creating files, and ensure the three main repositories (`kart_brain`, `kart_medulla`, `kart_docs`) are kept separated in their respective folders under the root.