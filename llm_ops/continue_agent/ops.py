from pathlib import Path
from ..utils import get_resource_content, WORKFLOW_FILES

def install_continue():
    print("⏩ Initializing Continue Agent Setup...")

    base_dir = Path.home() / ".continue"
    rules_dir = base_dir / "rules"
    prompts_dir = base_dir / "prompts"

    rules_dir.mkdir(parents=True, exist_ok=True)
    prompts_dir.mkdir(parents=True, exist_ok=True)

    # 1. Install Rules
    # Continue rules need frontmatter:
    # ---
    # description: ...
    # ---
    
    rules_map = {
        "clean-code.md": "Enforces clean code standards and tidy first principles.",
        "memory.md": "Maintains project history and evolution log."
    }

    for filename, description in rules_map.items():
        content = get_resource_content("rules", filename)
        final_content = f"---\ndescription: {description}\n---\n\n{content}"
        
        dest = rules_dir / filename
        dest.write_text(final_content, encoding="utf-8")
        print(f"   📜 Installed rule: ~/.continue/rules/{filename}")

    # 2. Install Prompts (Slash Commands)
    # Continue prompts need frontmatter:
    # ---
    # name: Prompt Name
    # description: Prompt description
    # invokable: true
    # ---

    for command, filename in WORKFLOW_FILES.items():
        content = get_resource_content("workflows", filename)
        
        # We need to parse the existing frontmatter (if any) or create new one
        # The existing workflows have:
        # ---
        # description: ...
        # ---
        
        # We need to adapt this to Continue's format
        description = "Custom command"
        if content.startswith("---"):
            end_index = content.find("---", 3)
            if end_index != -1:
                frontmatter = content[3:end_index].strip()
                for line in frontmatter.split('\n'):
                    if line.startswith("description:"):
                        description = line.replace("description:", "").strip()
                
                # Strip old frontmatter
                body = content[end_index+3:].strip()
            else:
                body = content
        else:
            body = content

        # Create new frontmatter
        name = command.replace("-", " ").title()
        new_frontmatter = (
            f"---\n"
            f"name: {name}\n"
            f"description: {description}\n"
            f"invokable: true\n"
            f"---\n\n"
        )
        
        final_content = new_frontmatter + body
        
        # Continue uses the filename as the ID, but the name in frontmatter for display
        dest = prompts_dir / filename
        dest.write_text(final_content, encoding="utf-8")
        print(f"   ⚡ Installed prompt: ~/.continue/prompts/{filename}")

    print("\n🚀 Continue agent installed.")

def uninstall_continue():
    print("🧹 Uninstalling Continue Agent...")

    base_dir = Path.home() / ".continue"
    rules_dir = base_dir / "rules"
    prompts_dir = base_dir / "prompts"

    # 1. Remove Rules
    if rules_dir.exists():
        for filename in ["clean-code.md", "memory.md"]:
            file_path = rules_dir / filename
            if file_path.exists():
                file_path.unlink()
                print(f"   🗑️  Removed rule: {filename}")

    # 2. Remove Prompts
    if prompts_dir.exists():
        for _, filename in WORKFLOW_FILES.items():
            file_path = prompts_dir / filename
            if file_path.exists():
                file_path.unlink()
                print(f"   🗑️  Removed prompt: {filename}")

    print("\n✨ Continue agent uninstalled.")
