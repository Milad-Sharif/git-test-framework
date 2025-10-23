
import pytest
import requests

# def test_add():
#     assert add(1, 2) == 3

# def test_subtract():
#     assert subtract(5, 3) == 2

# def test_divide():
#     assert divide(10, 2) == 5

# def test_divide_by_zero():
#     with pytest.raises(ValueError):
#         divide(10, 0)


@pytest.mark.parametrize("a, b, exp", [(1,2,3),(5,6,11),(99,1001,1100)])

def test_add_param(calc, a, b, exp):  
    assert calc.add(a, b) == exp


@pytest.mark.parametrize("a, b, exp", [(1,2,-1),(15,6,9),(99,1001,-902)])

def test_subtract_param(calc, a, b, exp):  
    assert calc.subtract(a, b) == exp


@pytest.mark.parametrize("a, b, exp", [(1,2,2),(5,6,30),(99,1001,99099)])

def test_multiplication_param(calc, a, b, exp):  
    assert calc.multiply(a, b) == pytest.approx(exp, rel=1e-3)


@pytest.mark.parametrize("a, b, exp", [(1,2,0.500000),(5,6,0.8333333),(99,1001,0.098901098)])

def test_divide_param(calc, a, b, exp):  
    assert calc.divide(a, b) == pytest.approx(exp, rel=1e-6)



