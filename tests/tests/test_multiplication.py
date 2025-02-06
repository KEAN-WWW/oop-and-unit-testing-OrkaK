"""Unit tests for multiplication function."""

from app.calculator import multiply

def test_multiply():
    """Tests multiplication functionality."""
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 10) == 0
