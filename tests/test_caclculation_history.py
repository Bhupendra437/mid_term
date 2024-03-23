# test_calculation_history.py

"""
Test suite for the CalculationHistory class.
"""

import os
import pandas as pd
from calculation_history import CalculationHistory

def test_initialization():
    """
    Test the initialization of the CalculationHistory class.
    """
    ch = CalculationHistory('test_history.csv')
    assert ch.filename == 'test_history.csv'
    assert ch.history.empty
    assert list(ch.history.columns) == ['Expression', 'Result']

def test_add_record():
    """
    Test adding a record to the calculation history.
    """
    ch = CalculationHistory('test_history.csv')
    ch.add_record('2 + 2', 4)
    assert not ch.history.empty
    assert ch.history.iloc[0]['Expression'] == '2 + 2'
    assert ch.history.iloc[0]['Result'] == 4

def test_save_and_load_history():
    """
    Test saving the history to a file and loading it back.
    """
    ch = CalculationHistory('test_history.csv')
    ch.add_record('3 + 3', 6)
    ch.save_history()

    new_ch = CalculationHistory('test_history.csv')
    new_ch.load_history()
    assert not new_ch.history.empty
    assert new_ch.history.iloc[0]['Expression'] == '3 + 3'
    assert new_ch.history.iloc[0]['Result'] == 6

    os.remove('test_history.csv')

def test_clear_history():
    """
    Test clearing the calculation history.
    """
    ch = CalculationHistory('test_history.csv')
    ch.add_record('4 + 4', 8)
    ch.clear_history()
    assert ch.history.empty

def test_delete_history():
    """
    Test deleting the history file and clearing the history.
    """
    ch = CalculationHistory('test_history.csv')
    ch.add_record('5 + 5', 10)
    ch.save_history()
    ch.delete_history()
    assert ch.history.empty
    assert not os.path.exists('test_history.csv')

def test_view_history():
    """
    Test viewing the calculation history.
    """
    ch = CalculationHistory('test_history.csv')
    ch.add_record('6 + 6', 12)
    view = ch.view_history()
    assert isinstance(view, pd.DataFrame)
    assert view.iloc[0]['Expression'] == '6 + 6'
    assert view.iloc[0]['Result'] == 12
    ch.delete_history()
