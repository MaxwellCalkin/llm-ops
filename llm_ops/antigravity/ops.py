from pathlib import Path
from ..utils import get_resource_content, WORKFLOW_FILES

def install_antigravity():
    print("🔮 Initializing Antigravity Setup...")
    
    # 1. Define Paths (Antigravity typical paths)
    base_dir = Path.home() / ".gemini"
    workflows_dir = base_dir / "antigravity" / "global_workflows"
    
    workflows_dir.mkdir(parents=True, exist_ok=True)

    # 2. Write Workflows (Raw Markdown)
    for command, filename in WORKFLOW_FILES.items():
        content = get_resource_content("workflows", filename)
        # Content already has frontmatter
        final_content = content
        
        dest = workflows_dir / filename
        dest.write_text(final_content, encoding="utf-8")
        print(f"   ✨ Installed workflow: {filename}")

    # 3. Write Memory File
    memory_content = get_resource_content("memory", "GEMINI.md")
    (base_dir / "GEMINI.md").write_text(memory_content, encoding="utf-8")
    
    print(f"   🧠 Installed memory: ~/.gemini/GEMINI.md")
    print("\n🚀 Antigravity installed. Point Antigravity to ~/.gemini/antigravity/global_workflows/")

def uninstall_antigravity():
    print("🧹 Uninstalling Antigravity...")
    
    # 1. Define Paths
    base_dir = Path.home() / ".gemini"
    workflows_dir = base_dir / "antigravity" / "global_workflows"
    
    # 2. Remove Workflows
    if workflows_dir.exists():
        for _, filename in WORKFLOW_FILES.items():
            file_path = workflows_dir / filename
            if file_path.exists():
                file_path.unlink()
                print(f"   🗑️  Removed workflow: {filename}")
        
        # Try to remove the directory if empty
        try:
            workflows_dir.rmdir()
        except OSError:
            pass # Directory not empty
            
    # 3. Remove Memory File
    memory_file = base_dir / "GEMINI.md"
    if memory_file.exists():
        memory_file.unlink()
        print(f"   🗑️  Removed memory: ~/.gemini/GEMINI.md")
        
    print("\n✨ Antigravity uninstalled.")
