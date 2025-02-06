import pytest
from app.calculator import divide

def test_division():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(-10, 2) == -5

    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
