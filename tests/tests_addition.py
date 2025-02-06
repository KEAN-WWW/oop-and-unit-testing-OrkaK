import pytest
from app.calculator import multiply

def test_multiplication():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 100) == 0
    assert multiply(10, 10) == 100

