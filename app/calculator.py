"""
Basic calculator functions for arithmetic operations.
"""

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """Returns the quotient of two numbers. Raises error if dividing by zero."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
