from typing import Any, Dict, cast

import requests


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the division of two numbers. Raise error if division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def get_exchange_rate(from_currency: str, to_currency: str) -> float:
    response = requests.get(
        f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    )
    data: Dict[str, Any] = response.json()
    return cast(float, data["rates"][to_currency])
