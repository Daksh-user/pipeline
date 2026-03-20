# test_main.py
import pytest
from main import add, subtract, multiply, divide, is_even, factorial

# --- add ---
def test_add():
    assert add(2, 4) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

# --- subtract ---
def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5

# --- multiply ---
def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 3) == -3

# --- divide ---
def test_divide():
    assert divide(6, 3) == 2
    with pytest.raises(ValueError):
        divide(5, 0)

# --- is_even ---
def test_is_even():
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(0) is True

# --- factorial ---
def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    with pytest.raises(ValueError):
        factorial(-1)