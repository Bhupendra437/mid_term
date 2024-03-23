"""Tests for the history module."""

import pytest
from app.plugins.calc.calculator.history import add_to_history, get_history, history

def test_add_to_history():
    """Test that add_to_history adds a record to the history."""
    # Clear the history before testing
    history.clear()

    # Add a record to the history
    add_to_history("2 + 2", 4)

    # Check that the record was added
    assert history == [{"expression": "2 + 2", "result": 4}]

def test_get_history():
    """Test that get_history returns the current history."""
    # Clear the history and add two records
    history.clear()
    add_to_history("2 + 2", 4)
    add_to_history("3 * 3", 9)

    # Check that get_history returns the correct history
    assert get_history() == [
        {"expression": "2 + 2", "result": 4},
        {"expression": "3 * 3", "result": 9},
    ]
