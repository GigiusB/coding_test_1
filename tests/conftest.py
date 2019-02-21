import sys
from pathlib import Path


def pytest_configure(config):
    here = Path(__file__).parent
    root = here.parent
    sys.path.insert(0, str(root / 'src'))