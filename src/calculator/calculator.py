import requests

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the division of two numbers. Raise error if division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def get_exchange_rate(from_currency, to_currency):
    response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{from_currency}")
    data = response.json()
    return data["rates"][to_currency]



