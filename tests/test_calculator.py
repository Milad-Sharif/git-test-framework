
import pytest
from src.calculator.calculator import add, subtract, multiply, divide

def test_add():
    assert add(1, 2) == 3

def test_subtract():
    assert subtract(5, 3) == 2

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


@pytest.mark.parametrize("a, b, exp", [(1,2,3),(5,6,11),(99,1001,1100)])

def test_add_param(a, b, exp):
    assert add(a, b) == exp
