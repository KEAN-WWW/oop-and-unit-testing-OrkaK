"""
Unit tests for the multiplication function.
"""

from app.calculator import multiply

def test_multiplication():
    """Test the multiplication function"""
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 100) == 0
