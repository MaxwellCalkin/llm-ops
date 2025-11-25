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
    # Note: We need to go up one level because this file is in llm_ops/
    # and resources are in llm_ops/resources/
    # But wait, utils.py is in llm_ops/, so resources is a sibling.
    # However, if we move this to a subpackage, we need to be careful.
    # Let's assume resources is always in llm_ops/resources
    
    # If this file is in llm_ops/utils.py
    resource_path = Path(__file__).parent / "resources" / subfolder / filename
    
    if not resource_path.exists():
        raise FileNotFoundError(f"Missing resource: {resource_path}")
    return resource_path.read_text(encoding="utf-8")
