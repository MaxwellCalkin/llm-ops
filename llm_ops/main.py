import argparse
import os
from pathlib import Path

# Mapping of command names to their source filenames
WORKFLOW_FILES = {
    "explain": "explain.md",
    "code-review": "code-review.md",
    "ask": "ask.md",
    "uncle-bob": "uncle-bob.md"
}

def get_resource_content(subfolder, filename):
    """Reads a file from the package resources."""
    # Locates the file relative to this script
    resource_path = Path(__file__).parent / "resources" / subfolder / filename
    if not resource_path.exists():
        raise FileNotFoundError(f"Missing resource: {resource_path}")
    return resource_path.read_text(encoding="utf-8")

def install_antigravity():
    print("🔮 Initializing Antigravity Setup...")
    
    # 1. Define Paths (Antigravity typical paths)
    base_dir = Path.home() / ".gemini"
    workflows_dir = base_dir / "antigravity" / "global_workflows"
    
    workflows_dir.mkdir(parents=True, exist_ok=True)

    # 2. Write Workflows (Raw Markdown)
    for command, filename in WORKFLOW_FILES.items():
        content = get_resource_content("workflows", filename)
        # Prepend specific description for Antigravity
        final_content = f"Description: {command} workflow.\n{content}"
        
        dest = workflows_dir / filename
        dest.write_text(final_content, encoding="utf-8")
        print(f"   ✨ Installed workflow: {filename}")

    # 3. Write Memory File
    memory_content = get_resource_content("memory", "GEMINI.md")
    (base_dir / "GEMINI.md").write_text(memory_content, encoding="utf-8")
    
    print(f"   🧠 Installed memory: ~/.gemini/GEMINI.md")
    print("\n🚀 Antigravity installed. Point Antigravity to ~/.gemini/antigravity/global_workflows/")
def install_augment():
    print("⚡ Initializing Augment Code Setup...")

    # 1. Define Paths (Augment standard global commands)
    base_dir = Path.home() / ".augment"
    commands_dir = base_dir / "commands"
    
    commands_dir.mkdir(parents=True, exist_ok=True)

    # 2. Write Commands (Needs Frontmatter for Augment)
    for command, filename in WORKFLOW_FILES.items():
        raw_content = get_resource_content("workflows", filename)
        
        # Augment requires Frontmatter
        frontmatter = f"""---
description: Run the {command} workflow
model: default
---

"""
        final_content = frontmatter + raw_content
        
        # Augment uses the filename as the command trigger (e.g. /explain)
        dest = commands_dir / filename
        dest.write_text(final_content, encoding="utf-8")
        print(f"   ⚡ Installed command: /{command} -> {dest}")

    # 3. Write Memory File (AGENTS.md)
    # Augment looks for AGENTS.md in the workspace, but we can stage a global copy
    memory_content = get_resource_content("memory", "AGENTS.md")
    (base_dir / "AGENTS.md").write_text(memory_content, encoding="utf-8")

    print(f"   🧠 Installed memory template: ~/.augment/AGENTS.md")
    print("   ℹ️  Note: Copy ~/.augment/AGENTS.md to your project root to activate memory.")
    print("\n🚀 Augment installed. Try typing '/uncle-bob' in your Augment chat.")

def main():
    parser = argparse.ArgumentParser(description="LLM-Ops CLI Tool")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Install command
    install_parser = subparsers.add_parser("install", help="Install components")
    install_parser.add_argument(
        "component", 
        choices=["antigravity", "augment"], 
        help="Component to install (antigravity for Windsurf, augment for Augment Code)"
    )

    args = parser.parse_args()

    if args.command == "install":
        if args.component == "antigravity":
            install_antigravity()
        elif args.component == "augment":
            install_augment()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
