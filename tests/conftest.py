import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from parser import MkDocstringsParser

import pytest


@pytest.fixture(scope="module")
def setup_parser():
    parser = MkDocstringsParser()
    yield parser
