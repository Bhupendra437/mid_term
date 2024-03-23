"""Tests for the Calculator operations."""

import pytest
from app.plugins.calc.calculator import Calculator

@pytest.mark.parametrize('num1, num2, operation, expected', [
    (2, 2, 'add', 4),
    (3, 3, 'multiply', 9),
    (5, 2, 'subtract', 3),
    (6, 3, 'divide', 2),
])
def test_operation(num1, num2, operation, expected):
    """
    Test the Calculator operations with various inputs and expected results.
    """
    operation_mappings = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide,
    }

    operation_function = operation_mappings.get(operation)
    result = operation_function(num1, num2)
    assert result == expected
