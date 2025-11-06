import pytest
from calculator import calculator


@pytest.fixture
def calc() -> calculator:
    return calculator  # Reusable calculator module for all the tests.
