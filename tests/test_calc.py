"""Tests for the CalcCommand class."""

from decimal import Decimal
from unittest.mock import patch, MagicMock
import pytest
from app.plugins.calc import CalcCommand

@pytest.mark.parametrize('args, expected_output', [
    (['2', '2', '+'], "The result of 2 + 2 is equal to 4"),
    (['3', '3', '*'], "The result of 3 * 3 is equal to 9"),
    (['5', '2', '-'], "The result of 5 - 2 is equal to 3"),
    (['6', '3', '/'], "The result of 6 / 3 is equal to 2"),
    (['invalid', '2', '+'], "Invalid number input: invalid or 2 is not a valid number."),
    (['2', '2', 'unknown'], "Unknown operation: unknown"),
    (['2'], "Usage: calc <number1> <number2> <operation>"),
])
def test_calc_command(args, expected_output, capsys):
    """
    Test the CalcCommand class with various input arguments and expected outputs.
    """
    # Create a mock CalculationHistory object
    mock_calculation_history = MagicMock()

    # Instantiate CalcCommand with the mock CalculationHistory
    calc_command = CalcCommand(mock_calculation_history)

    # Execute the command with the provided arguments
    calc_command.execute(args)

    # Capture the output
    captured = capsys.readouterr()

    # Check if the output matches the expected output
    assert captured.out.strip() == expected_output
