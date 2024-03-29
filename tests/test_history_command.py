"""Tests for the HistoryCommand class."""

from unittest.mock import MagicMock
import pandas as pd
import pytest
from app.plugins.calchistory import HistoryCommand

def test_history_command_with_empty_history(capsys):
    """
    Test the HistoryCommand class with an empty calculation history.
    It should print a message indicating that no history is available.
    """
    # Create a mock CalculationHistory object with an empty history
    mock_calculation_history = MagicMock()
    mock_calculation_history.view_history.return_value = pd.DataFrame()

    # Instantiate HistoryCommand with the mock CalculationHistory
    history_command = HistoryCommand(mock_calculation_history)

    # Execute the command
    history_command.execute([])

    # Capture the output
    captured = capsys.readouterr()

    # Check if the output indicates that there is no history available
    assert captured.out.strip() == "No history available."

def test_history_command_with_non_empty_history(capsys):
    """
    Test the HistoryCommand class with a non-empty calculation history.
    It should print the history.
    """
    # Create a mock CalculationHistory object with some history
    mock_calculation_history = MagicMock()
    history_df = pd.DataFrame({'Expression': ['2 + 2', '3 * 3'], 'Result': [4, 9]})
    mock_calculation_history.view_history.return_value = history_df

    # Instantiate HistoryCommand with the mock CalculationHistory
    history_command = HistoryCommand(mock_calculation_history)

    # Execute the command
    history_command.execute([])

    # Capture the output
    captured = capsys.readouterr()

    # Check if the output contains the history
    assert "2 + 2 = 4" in captured.out
    assert "3 * 3 = 9" in captured.out
