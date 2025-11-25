import pytest
from unittest.mock import MagicMock, patch, call
from pathlib import Path
import sys

# Updated imports based on project structure
from llm_ops.utils import get_resource_content, WORKFLOW_FILES
from llm_ops.antigravity.ops import install_antigravity
from llm_ops.augment.ops import install_augment
from llm_ops.main import main

# --- Unit Tests ---

def test_get_resource_content_success():
    """Test reading an existing resource file."""
    with patch("llm_ops.utils.Path") as MockPath:
        mock_file = MagicMock()
        mock_file.exists.return_value = True
        mock_file.read_text.return_value = "content"
        
        # Mock the parent chain: Path(__file__).parent / "resources" / subfolder / filename
        MockPath.return_value.parent.__truediv__.return_value.__truediv__.return_value.__truediv__.return_value = mock_file
        
        content = get_resource_content("workflows", "explain.md")
        assert content == "content"

def test_get_resource_content_not_found():
    """Test that FileNotFoundError is raised for missing files."""
    with patch("llm_ops.utils.Path") as MockPath:
        mock_file = MagicMock()
        mock_file.exists.return_value = False
        
        MockPath.return_value.parent.__truediv__.return_value.__truediv__.return_value.__truediv__.return_value = mock_file
        
        with pytest.raises(FileNotFoundError):
            get_resource_content("workflows", "nonexistent.md")

# --- Integration Tests (Mocked) ---

@patch("llm_ops.antigravity.ops.Path")
@patch("llm_ops.antigravity.ops.get_resource_content")
def test_install_antigravity(mock_get_resource, MockPath):
    """Test the install_antigravity function."""
    mock_home = MagicMock()
    MockPath.home.return_value = mock_home
    mock_get_resource.return_value = "mock_content"
    
    install_antigravity()
    
    # Verify resource fetching
    assert mock_get_resource.call_count == len(WORKFLOW_FILES) + 1 # +1 for GEMINI.md
    
    # Verify specific calls
    mock_get_resource.assert_any_call("memory", "GEMINI.md")
    for filename in WORKFLOW_FILES.values():
        mock_get_resource.assert_any_call("workflows", filename)

@patch("llm_ops.augment.ops.Path")
@patch("llm_ops.augment.ops.get_resource_content")
def test_install_augment(mock_get_resource, MockPath):
    """Test the install_augment function."""
    mock_home = MagicMock()
    MockPath.home.return_value = mock_home
    mock_get_resource.return_value = "mock_content"
    
    install_augment()
    
    # Verify resource fetching
    assert mock_get_resource.call_count == len(WORKFLOW_FILES) + 1 # +1 for AGENTS.md
    
    mock_get_resource.assert_any_call("memory", "AGENTS.md")
    for filename in WORKFLOW_FILES.values():
        mock_get_resource.assert_any_call("workflows", filename)

@patch("llm_ops.main.install_antigravity")
def test_main_cli_install_antigravity(mock_install):
    """Test CLI install antigravity command."""
    with patch.object(sys, 'argv', ["llm-ops", "install", "antigravity"]):
        main()
        mock_install.assert_called_once()

@patch("llm_ops.main.install_augment")
def test_main_cli_install_augment(mock_install):
    """Test CLI install augment command."""
    with patch.object(sys, 'argv', ["llm-ops", "install", "augment"]):
        main()
        mock_install.assert_called_once()
