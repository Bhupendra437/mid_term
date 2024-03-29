"""Tests for the HistoryReplCommand class."""

from unittest.mock import patch, MagicMock
import pytest
from app.plugins.historyrepl import HistoryReplCommand

@pytest.mark.parametrize('user_input, expected_output', [
    (['load', 'exit'], "History loaded."),
    (['save', 'exit'], "History saved."),
    (['add', 'expression', 'result', 'exit'], "Record added."),
    (['clear', 'exit'], "History cleared."),
    (['delete', 'exit'], "History deleted."),
    (['view', 'exit'], ""),
    (['invalid', 'exit'], "Invalid choice. Please try again."),
])
def test_history_repl_command(user_input, expected_output):
    """
    Test the HistoryReplCommand class with different user inputs and expected outputs.
    """
    # Create a mock CalculationHistory object
    mock_calculation_history = MagicMock()

    # Instantiate HistoryReplCommand with the mock CalculationHistory
    history_repl_command = HistoryReplCommand(mock_calculation_history)

    with patch('builtins.input', side_effect=user_input), patch('builtins.print') as mock_print:
        history_repl_command.execute([])

        # Check if the expected output was printed
        if expected_output:
            mock_print.assert_any_call(expected_output)
