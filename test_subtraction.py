"""Unit tests for subtraction function."""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.calculator import subtract

def test_subtract():
    """Tests subtraction functionality."""
    assert subtract(5, 3) == 2
    assert subtract(0, 4) == -4
    assert subtract(7, 7) == 0
