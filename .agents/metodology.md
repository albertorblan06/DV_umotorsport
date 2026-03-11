# Agent Methodology and Project Continuation Guide

This file contains the core instructions and constraints for any CLI agent working on the `umotorsport` project. Every new session or autonomous agent must read and strictly adhere to this document before making any changes.

## 1. Strict Constraints
- **NO EMOJIS:** Do not use emojis in any communication with the user, in code comments, in markdown files, or in commit messages. Keep the tone professional, concise, and direct.
- **Project Structure:** The root `umotorsport` directory contains three primary repositories: `kart_brain`, `kart_medulla`, and `kart_docs`. Maintain this structure. Always check absolute paths before running commands.

## 2. Project Resumption Protocol
When a new agent session starts, it must execute the following steps to understand the project state:
1. **Read `umotorsport/TODO.md`:** This is the source of truth for all current tasks, sorted by priority. Identify the highest priority task marked as pending.
2. **Read `umotorsport/.agents/errors.md`:** Review the historical errors made by previous agents to ensure you do not repeat the same mistakes.
3. **Analyze Workspace:** Navigate into the relevant sub-repository (`kart_brain`, `kart_medulla`, or `kart_docs`) and analyze the current branch, uncommitted changes (using `git status` and `git diff`), and relevant files to understand where the previous session left off.
4. **Plan & Confirm:** Present a concise plan of action based on the findings from the TODO list and workspace analysis before proceeding with implementation.

## 3. Task Execution and Roadmap Generation (CRITICAL)
- **Numbered Iteration Roadmaps:** Every time a new iteration or milestone starts, the agent MUST create a new numbered roadmap file (e.g., `1.md`, `2.md`, etc.) in the `kart_docs/docs/iterations/` directory to preserve the history of past iterations. Do NOT overwrite past roadmaps.
- **Update MkDocs:** After creating a new iteration roadmap, update the `nav` section in `kart_docs/mkdocs.yml` and the links in `kart_docs/docs/iterations/index.md` so the new iteration is visible on the website.
- **Detailed Breakdowns:** This file must contain a detailed, step-by-step breakdown of how the task will be executed. The agent must update this roadmap as steps are completed.
- **Diagnostic Unit Testing:** When encountering an error, or when a component is not working as expected, the agent must NOT guess the problem. Instead, the agent MUST write and execute isolated Python unit test scripts (or equivalent diagnostic C/C++ test files) to systematically pinpoint the exact point of failure before attempting a fix.

## 4. Error Tracking and Documentation
Whenever an agent makes a mistake (e.g., a buggy script, a failed build, a compilation error due to a bad assumption, or deleting something by accident), the agent MUST document it in `.agents/errors.md`.

The entry must include:
- **Context:** What the agent was trying to achieve.
- **The Error:** What went wrong (the stack trace, the failed command, the bug).
- **The Resolution/Lesson:** How it was fixed and what the agent must do in the future to avoid repeating the mistake.

## 5. Commit Policy
- **Commit after every change.** Every time a meaningful change is completed (a fix applied, a file created, a feature added), the agent MUST immediately stage and commit the affected files with a clear, concise commit message. Do not batch multiple unrelated changes into a single commit. Do not wait until the end of a session to commit.
- Follow the commit protocol in `kart_brain/AGENTS.md`: run `git status`, review with `git diff --cached`, then commit.

## 6. Work Execution
- When fixing an issue, always attempt to build or run the affected component to verify it works (e.g., `colcon build` for ROS2 in `kart_brain`, `idf.py build` for ESP-IDF in `kart_medulla`).
- Keep tasks small and incremental.
- Do not make sweeping assumptions about hardware constraints; read the existing configuration files or `TODO.md` for context.