import argparse
from llm_ops.antigravity.ops import install_antigravity, uninstall_antigravity
from llm_ops.augment.ops import install_augment, uninstall_augment

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

    # Uninstall command
    uninstall_parser = subparsers.add_parser("uninstall", help="Uninstall components")
    uninstall_parser.add_argument(
        "component", 
        choices=["antigravity", "augment"], 
        help="Component to uninstall"
    )

    args = parser.parse_args()

    if args.command == "install":
        if args.component == "antigravity":
            install_antigravity()
        elif args.component == "augment":
            install_augment()
    elif args.command == "uninstall":
        if args.component == "antigravity":
            uninstall_antigravity()
        elif args.component == "augment":
            uninstall_augment()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
