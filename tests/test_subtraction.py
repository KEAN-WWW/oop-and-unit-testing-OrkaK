"""
Unit tests for the subtraction function.
"""

from app.calculator import subtract

def test_subtraction():
    """Test the subtraction function"""
    assert subtract(5, 3) == 2
    assert subtract(10, 10) == 0
    assert subtract(0, 5) == -5
