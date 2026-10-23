"""Behavioral tests for the demo calculator."""

import pytest

from calculator import divide


def test_divide_returns_quotient():
    assert divide(8, 2) == 4


def test_divide_supports_fractional_results():
    assert divide(3, 2) == 1.5


def test_divide_rejects_zero_denominator():
    with pytest.raises(ValueError, match="cannot divide by zero"):
        divide(1, 0)
