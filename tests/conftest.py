
import pytest
from calculator import calculator

@pytest.fixture
def calc():
    return calculator #Reusable calculator module for all the tests.

