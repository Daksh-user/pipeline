# test_main.py

from main import add
# --- add ---
def test_add():
    assert add(2, 89) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

# --- subtract ---
