# core-engine/README.py

__version__ = "1.0.0"

from pathlib import Path

def get_project_root():
    """Returns the project root directory."""
    return Path(__file__).parent.parent

def get_dependencies():
    """Returns a dictionary of project dependencies."""
    dependencies = {
        "core": "1.0.0",
        "utils": "2.0.0"
    }
    return dependencies

def get_contributors():
    """Returns a list of project contributors."""
    contributors = [
        "John Doe <john.doe@example.com>",
        "Jane Doe <jane.doe@example.com>"
    ]
    return contributors

def get_license():
    """Returns the project license."""
    return "Apache License 2.0"

def get_usage():
    """Returns a string describing how to use the project."""
    return "Usage: python -m core-engine"