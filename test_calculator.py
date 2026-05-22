"""Test suite for the calculator module."""

import pytest
from calculator import calculate, format_result


class TestCalculate:
    """Test cases for the calculate function."""

    def test_addition(self):
        """Test addition operation."""
        assert calculate(5, 3, '+') == 8
        assert calculate(-5, 3, '+') == -2
        assert calculate(0, 0, '+') == 0

    def test_subtraction(self):
        """Test subtraction operation."""
        assert calculate(10, 3, '-') == 7
        assert calculate(5, 10, '-') == -5
        assert calculate(0, 5, '-') == -5

    def test_multiplication(self):
        """Test multiplication operation."""
        assert calculate(4, 5, '*') == 20
        assert calculate(-3, 4, '*') == -12
        assert calculate(0, 100, '*') == 0

    def test_division(self):
        """Test division operation."""
        assert calculate(10, 2, '/') == 5
        assert calculate(15, 3, '/') == 5
        assert calculate(-20, 4, '/') == -5

    def test_division_by_zero(self):
        """Test division by zero raises ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError):
            calculate(5, 0, '/')

    def test_unsupported_operator(self):
        """Test unsupported operator raises ValueError."""
        with pytest.raises(ValueError):
            calculate(5, 3, '%')
        with pytest.raises(ValueError):
            calculate(5, 3, '^')


class TestFormatResult:
    """Test cases for the format_result function."""

    def test_format_integer_result(self):
        """Test formatting with integer results."""
        assert format_result(5, 3, '+', 8) == "5 + 3 = 8"
        assert format_result(10, 2, '/', 5) == "10 / 2 = 5"

    def test_format_float_result(self):
        """Test formatting with float results."""
        assert format_result(5, 3, '/', 1.6666666666666667) == "5 / 3 = 1.6666666666666667"

    def test_format_negative_numbers(self):
        """Test formatting with negative numbers."""
        assert format_result(-5, 3, '+', -2) == "-5 + 3 = -2"
        assert format_result(5, -3, '*', -15) == "5 * -3 = -15"
