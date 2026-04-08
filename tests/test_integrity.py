import os
import pytest

def test_essential_documentation_exists():
    essential_files = [
        'README.md', 'LICENSE', 'CITATION.cff', 'CODE_OF_CONDUCT.md',
        'CONTRIBUTING.md', 'SECURITY.md', 'GOVERNANCE.md'
    ]
    for ef in essential_files:
        assert os.path.exists(ef), f"{ef} missing"

def test_data_directories():
    dirs = ['data/raw', 'data/clean', 'data/analysis_ready']
    for d in dirs:
        assert os.path.isdir(d), f"{d} is not a directory"
