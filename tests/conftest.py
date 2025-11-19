import pytest

from mkdocstrings_parser import MkDocstringsParser


@pytest.fixture(scope="module")
def setup_parser():
    parser = MkDocstringsParser()
    yield parser
