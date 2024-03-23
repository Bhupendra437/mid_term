"""
This module contains tests for the calculator operations and Calculation class.

The tests are designed to verify the correctness of basic arithmetic operations
(addition, subtraction, multiplication, division) implemented in the calculator.operations module,
as well as the functionality of the Calculation class that encapsulates these operations.
"""

from decimal import Decimal
import pytest
from app.plugins.calc.calculator.calculation import Calculation
from app.plugins.calc.calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize('num1, num2, operation, expected', [
    (Decimal('2'), Decimal('2'), add, Decimal('4')),
    (Decimal('3'), Decimal('3'), multiply, Decimal('9')),
    (Decimal('5'), Decimal('2'), subtract, Decimal('3')),
    (Decimal('6'), Decimal('3'), divide, Decimal('2')),
    # Add more test cases as needed
])
def test_calculation_operations(num1, num2, operation, expected):
    """
    Test calculation operations with various scenarios.

    This test ensures that the Calculation class correctly performs the arithmetic operation
    (specified by the 'operation' parameter) on two Decimal operands ('num1' and 'num2'),
    and that the result matches the expected outcome.
    """
    calc = Calculation(num1, num2, operation)
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {num1} and {num2}"

def test_calculation_repr():
    """
    Test the string representation (__repr__) of the Calculation class.

    This test verifies that the repr function returns a string
    that accurately represents the state of the Calculation object, including its operands and operation.
    """
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation(10, 5, add)"
    assert repr(calc) == expected_repr, "The repr function output does not match the expected string."

def test_divide_by_zero():
    """
    Test division by zero to ensure it raises a ValueError.

    This test checks that attempting to perform a division operation with a zero divisor
    correctly raises a ValueError, as dividing by zero is mathematically undefined and should be handled as an error.
    """
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()
