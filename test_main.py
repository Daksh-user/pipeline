# test_main.py

from main import add,subtract, multiply, divide, is_even, factorial

# --- add ---
def test_add():
    assert add(2, 4) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

# --- subtract ---
