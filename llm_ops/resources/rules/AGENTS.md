# AGENT INSTRUCTIONS

## 1. Code Style & Philosophy
* **Philosophy:** Uncle Bob's "Clean Code" & Kent Beck's "Tidy First".
* **Expectations:** Small functions, clear naming, DRY, high test coverage, etc.

## 2. Project Memory (AGENTS.md)
You are responsible for maintaining your own context and history in this file (`AGENTS.md`) at the root of the project.

**Protocol:**
1.  **Update Loop:** After completing a significant command or `Edit`, update this file with a brief summary of what changed and *why*.
2.  **Context Management:** Augment has a large context window, but don't abuse it. Keep this file structured with:
    * **## Current State:** High-level architectural summary.
    * **## Change Log:** Chronological list of recent major shifts.
3.  **Pruning:** When the Change Log exceeds 100 lines, summarize the oldest 50 lines into the "Current State" section and delete them from the log.
