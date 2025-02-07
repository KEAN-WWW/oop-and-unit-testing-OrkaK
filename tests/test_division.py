"""
Unit tests for the division function.
"""

import pytest
from app.calculator import divide

def test_divide():
    """Test normal division cases"""
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(7, 1) == 7

def test_divide_zero_exception():
    """Test division by zero raises ZeroDivisionError"""
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
