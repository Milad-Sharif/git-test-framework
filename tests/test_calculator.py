import pytest
from calculator import calculator as calc


@pytest.mark.parametrize("a, b, exp", [(1, 2, 3), (5, 6, 11), (99, 1001, 1100)])
def test_add_param(calc, a: float, b: float, exp: float) -> None:
    assert calc.add(a, b) == exp


@pytest.mark.parametrize("a, b, exp", [(1, 2, -1), (15, 6, 9), (99, 1001, -902)])
def test_subtract_param(calc, a: float, b: float, exp: float) -> None:
    assert calc.subtract(a, b) == exp


@pytest.mark.parametrize("a, b, exp", [(1, 2, 2), (5, 6, 30), (99, 1001, 99099)])
def test_multiplication_param(calc, a: float, b: float, exp: float) -> None:
    assert calc.multiply(a, b) == pytest.approx(exp, rel=1e-3)


@pytest.mark.parametrize(
    "a, b, exp", [(1, 2, 0.500000), (5, 6, 0.8333333), (99, 1001, 0.098901098)]
)
def test_divide_param(calc, a: float, b: float, exp: float) -> None:
    assert calc.divide(a, b) == pytest.approx(exp, rel=1e-6)


def test_divide_by_zero() -> None:
    with pytest.raises(ValueError) as excinfo:
        calc.divide(10, 0)
    assert "Cannot divide by zero" in str(excinfo.value)


def test_divide_negative() -> None:
    result = calc.divide(10, -2)
    assert result == -5
