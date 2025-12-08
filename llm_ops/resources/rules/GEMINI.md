# GLOBAL AGENT PROTOCOL

## 1. Engineering Standards
When editing or analyzing code in any project, you must adhere to:
* **Clean Code (Robert C. Martin):** readable, small functions, meaningful names, DRY, etc.
* **Tidy First (Kent Beck):** Make the change easy, then make the easy change.

## 2. The "Memory" Protocol (Change Logging)
You are responsible for maintaining a history of the codebase evolution in a file named `GEMINI.md` in the root of the *current project*.

**Rules:**
1.  **Create if Missing:** If `GEMINI.md` does not exist, create it.
2.  **Log Changes:** After every significant code edit, append a summary entry.
3.  **Compression:** If `GEMINI.md` > 50 lines, condense older history into a summary block.
