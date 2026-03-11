# Methodology and Development Rules

Core instructions and constraints for all agents and developers on the DV_umotorsport project. Read and adhere to this document before making any changes.

## 1. Strict Constraints

- **No emojis.** Not in code, comments, markdown, commit messages, or communication. Professional, concise, direct.
- **Monorepo structure.** The root `DV_umotorsport/` contains three subsystems: `kart_brain/`, `kart_medulla/`, `kart_docs/`. Maintain this structure. Always verify absolute paths before running commands.
- **All agent/dev knowledge lives in `.agents/`.** Do not create per-repo AGENTS.md, CLAUDE.md, or GEMINI.md files. The root `.agents/README.md` is the single entry point.

## 2. Session Resumption Protocol

When a new agent session starts:

1. **Read `.agents/README.md`** -- the entry point that references all other files.
2. **Read `TODO.md`** -- source of truth for current tasks, sorted by priority. Identify the highest priority pending task.
3. **Read `.agents/errors.md`** -- review past mistakes to avoid repeating them.
4. **Analyze workspace** -- check `git status`, `git diff`, and relevant files to understand where the previous session left off.
5. **Plan and confirm** -- present a concise plan of action before proceeding with implementation.

## 3. GSD Workflow

This project uses **GSD (Get Shit Done)** for structured planning and execution. Configuration is in `.planning/config.json`.

Key commands:
- `/gsd-new-project` -- Create project roadmap
- `/gsd-plan-phase` -- Plan a phase
- `/gsd-execute-phase` -- Execute a phase
- `/gsd-settings` -- Configure GSD

## 4. Task Execution

- **Numbered iteration roadmaps:** When a new iteration or milestone starts, create a numbered roadmap file (e.g., `1.md`, `2.md`) in `kart_docs/docs/iterations/` to preserve history. Do NOT overwrite past roadmaps.
- **Update MkDocs:** After creating a new iteration roadmap, update `kart_docs/mkdocs.yml` nav and `kart_docs/docs/iterations/index.md`.
- **Diagnostic testing:** When encountering an error, do NOT guess. Write and execute isolated test scripts to pinpoint the exact failure before attempting a fix.
- **Keep tasks small and incremental.** Do not make sweeping assumptions about hardware constraints; read configuration files and `TODO.md` for context.

## 5. Error Tracking

Whenever an agent makes a mistake (buggy script, failed build, bad assumption, accidental deletion), document it in `.agents/errors.md` with:

- **Date/Session**
- **Context:** What was being attempted
- **The Error:** What went wrong (stack trace, failed command, bug)
- **The Resolution/Lesson:** How it was fixed and what to do in the future

## 6. Commit Policy

- **Commit after every meaningful change.** A fix applied, a file created, a feature added -- stage and commit immediately with a clear, concise message. Do not batch unrelated changes. Do not wait until end of session.
- **Commit protocol:**
  1. `git status` -- check what will be committed
  2. `git diff --cached` -- review staged changes
  3. Build/verify on the target machine before committing
  4. If a mistake occurred, document it in `.agents/errors.md`

## 7. Definition of Done

A change is NOT done until validated on the target machine:
- Code pushed? Pull on Orin/VM too.
- ESP32 firmware? Flash it.
- Python/launch change? Restart affected nodes.
- Dashboard change? Verify in the browser with actual values.
- Never claim something is fixed if you only pushed -- deploy and verify.

## 8. Environment Rules

- **Environment is in `.bashrc`** on every machine. ROS, workspace, and `IGN_GAZEBO_RESOURCE_PATH` are all sourced automatically. Never tell the user to source or export these manually.
- **All hardware (ESP32, cameras, actuators) is on the Orin.** The Mac is for development only. Never try to interact with kart hardware from the Mac.
- **After creating/modifying files under `src/`, scp to the target and rebuild.** Files in `src/` are not used directly -- only installed copies in `install/` are.

## 9. Documentation Rules

- **Document every decision.** Version choices, workarounds, approach selections -- write them in the relevant `.agents/` file with date and reasoning.
- **Document every error** in `.agents/errors.md`.
- **Document every version.** Software versions, SDK versions, wheel sources, compatibility notes -- go in the relevant environment file.
- **Official docs live in `kart_docs/`.** The `.agents/` directory is for AI agent workflow and developer reference, not official project documentation.
