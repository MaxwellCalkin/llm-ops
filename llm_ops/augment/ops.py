from pathlib import Path
from ..utils import get_resource_content, WORKFLOW_FILES

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

def uninstall_augment():
    print("🧹 Uninstalling Augment Code...")

    # 1. Define Paths
    base_dir = Path.home() / ".augment"
    commands_dir = base_dir / "commands"
    
    # 2. Remove Commands
    if commands_dir.exists():
        for _, filename in WORKFLOW_FILES.items():
            file_path = commands_dir / filename
            if file_path.exists():
                file_path.unlink()
                print(f"   🗑️  Removed command: /{filename}")
        
        # Try to remove the directory if empty
        try:
            commands_dir.rmdir()
        except OSError:
            pass # Directory not empty

    # 3. Remove Memory File
    memory_file = base_dir / "AGENTS.md"
    if memory_file.exists():
        memory_file.unlink()
        print(f"   🗑️  Removed memory: ~/.augment/AGENTS.md")

    print("\n✨ Augment uninstalled.")
