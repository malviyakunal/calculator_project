import pytest
import sys
import os


# This line makes sure Python can find your src/ folder
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()
