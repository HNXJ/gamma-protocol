import os
import subprocess
import pytest

def test_forge_scientific():
    """Verify that the forge generates a correct scientific GAMMA trace."""
    cmd = [
        "python3", "src/gamma_protocol/forge.py",
        "--mode", "scientific",
        "--title", "Test Scientific",
        "--problem", "How to test?",
        "--solution", "Use pytest.",
        "--logic", "Run command."
    ]
    subprocess.run(cmd, check=True)
    
    filename = "test_scientific.gamma"
    assert os.path.exists(filename)
    
    with open(filename, "r") as f:
        content = f.read()
        assert "**mode**: scientific" in content
        assert "### 🧬 Scientific Mode" in content
        assert "- **Research Question**: How to test?" in content
    
    os.remove(filename)

def test_forge_debug():
    """Verify that the forge generates a correct debugging GAMMA trace."""
    cmd = [
        "python3", "src/gamma_protocol/forge.py",
        "--mode", "debug",
        "--title", "Test Debug",
        "--problem", "Failure found.",
        "--solution", "Broken logic.",
        "--logic", "Apply fix.",
        "--repro", "Run script.",
        "--patch", "Change line 10.",
        "--validation", "Success."
    ]
    subprocess.run(cmd, check=True)
    
    filename = "test_debug.gamma"
    assert os.path.exists(filename)
    
    with open(filename, "r") as f:
        content = f.read()
        assert "**mode**: debug" in content
        assert "### 🛠 Debugging Mode" in content
        assert "- **Observed vs. Expected**: Failure found." in content
        assert "- **Reproduction**: Run script." in content
    
    os.remove(filename)
