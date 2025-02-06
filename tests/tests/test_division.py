"""Unit tests for division function."""

from app.calculator import divide

def test_divide():
    """Tests division functionality."""
    assert divide(6, 2) == 3
    assert divide(9, -3) == -3
    assert divide(5, 2) == 2.5
