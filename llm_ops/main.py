import argparse
import subprocess
import sys
from pathlib import Path
from llm_ops.antigravity.ops import install_antigravity, uninstall_antigravity
from llm_ops.augment.ops import install_augment, uninstall_augment
from llm_ops.continue_agent.ops import install_continue, uninstall_continue

def reload_package():
    """Rebuild and reinstall the llm-ops package for development."""
    print("🔄 Reloading llm-ops package...")
    
    # Get the project root (where pyproject.toml is)
    project_root = Path(__file__).parent.parent
    
    # Check if running from installed package or source
    pyproject_file = project_root / "pyproject.toml"
    if not pyproject_file.exists():
        print("❌ Error: reload command must be run from the source directory")
        print("   Try: cd to your llm-ops source directory and run 'uv run python -m llm_ops.main reload'")
        print("   Or:  'uv build && uv tool install --force .'")
        sys.exit(1)
    
    try:
        # Clean build artifacts
        print("   🧹 Cleaning build artifacts...")
        import shutil
        for dir_name in ["build", "dist", "llm_ops.egg-info"]:
            dir_path = project_root / dir_name
            if dir_path.exists():
                shutil.rmtree(dir_path)
        
        # Build the package
        print("   🔨 Building package...")
        result = subprocess.run(
            ["uv", "build"],
            cwd=project_root,
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            print(f"❌ Build failed:\n{result.stderr}")
            sys.exit(1)
        
        # Uninstall existing tool to avoid cache issues
        print("   🗑️  Uninstalling existing package...")
        result = subprocess.run(
            ["uv", "tool", "uninstall", "llm-ops"],
            cwd=project_root,
            capture_output=True,
            text=True
        )
        # Don't fail if package wasn't installed - that's okay
        
        # Install the newly built wheel
        print("   📦 Installing package...")
        result = subprocess.run(
            ["uv", "tool", "install", str(project_root / "dist" / "llm_ops-0.1.0-py3-none-any.whl")],
            cwd=project_root,
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            print(f"❌ Installation failed:\n{result.stderr}")
            sys.exit(1)
        
        print("✅ Package reloaded successfully!")
        print("\n💡 Run 'llm-ops install <component>' to apply changes")
        
    except FileNotFoundError:
        print("❌ Error: 'uv' command not found. Please ensure uv is installed.")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error during reload: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="LLM-Ops CLI Tool")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Install command
    install_parser = subparsers.add_parser("install", help="Install components")
    install_parser.add_argument(
        "component", 
        choices=["antigravity", "augment", "continue"], 
        help="Component to install (antigravity, augment, or continue)"
    )

    # Uninstall command
    uninstall_parser = subparsers.add_parser("uninstall", help="Uninstall components")
    uninstall_parser.add_argument(
        "component", 
        choices=["antigravity", "augment", "continue"], 
        help="Component to uninstall"
    )

    # Reload command
    subparsers.add_parser("reload", help="Rebuild and reinstall the llm-ops package (for development)")

    args = parser.parse_args()

    if args.command == "install":
        if args.component == "antigravity":
            install_antigravity()
        elif args.component == "augment":
            install_augment()
        elif args.component == "continue":
            install_continue()
    elif args.command == "uninstall":
        if args.component == "antigravity":
            uninstall_antigravity()
        elif args.component == "augment":
            uninstall_augment()
        elif args.component == "continue":
            uninstall_continue()
    elif args.command == "reload":
        reload_package()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
