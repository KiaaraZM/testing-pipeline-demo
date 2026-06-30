"""Test suite for calculator.py — runs identically on all 5 CI/CD tools."""
import pytest
from app.calculator import add, subtract, multiply, divide


class TestAdd:
    def test_positive_numbers(self):
        assert add(2, 3) == 5

    def test_negative_numbers(self):
        assert add(-1, -1) == -2

    def test_mixed_sign(self):
        assert add(-5, 10) == 5

    def test_zero(self):
        assert add(0, 0) == 0


class TestSubtract:
    def test_basic(self):
        assert subtract(10, 4) == 6

    def test_result_negative(self):
        assert subtract(3, 10) == -7


class TestMultiply:
    def test_basic(self):
        assert multiply(3, 4) == 12

    def test_by_zero(self):
        assert multiply(5, 0) == 0

    def test_negatives(self):
        assert multiply(-2, 3) == -6


class TestDivide:
    def test_basic(self):
        assert divide(10, 2) == 5.0

    def test_float_result(self):
        assert divide(7, 2) == 3.5

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)
