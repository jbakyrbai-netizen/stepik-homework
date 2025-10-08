import math
import pytest

def test_abs_function():
    assert abs(-42) == 42

def test_math_log():
    assert math.isclose(math.log(1), 0)
