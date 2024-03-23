# test_main.py
"""
Test suite for the CalculatorREPL class in main.py.
"""

from unittest.mock import patch, MagicMock
import pytest
from main import CalculatorREPL
from app.commands import CommandHandler, Command
from app.plugins.menu import MenuCommand

class MockCommand(Command):
    """A mock command for testing."""
    def execute(self, args):
        print("MockCommand output")

def test_command_handler_execute_known_command():
    """
    Test executing a known command in CommandHandler.
    """
    command_handler = CommandHandler()
    with patch('tests.test_main.MockCommand.execute', side_effect=lambda args: print("MockCommand output")) as mock_execute:
        command_handler.register_command('test', MockCommand())
        with patch('builtins.print') as mock_print:
            command_handler.execute_command('test', [])
            mock_execute.assert_called_once_with([])
            mock_print.assert_called_once_with("MockCommand output")

def test_command_handler_execute_unknown_command():
    """
    Test executing an unknown command in CommandHandler.
    """
    command_handler = CommandHandler()
    with patch('builtins.print') as mock_print:
        command_handler.execute_command('unknown', [])
        mock_print.assert_called_once_with("No such command: unknown")

def test_menu_command_test_mode():
    """
    Test the MenuCommand with the 'test_mode' argument.
    """
    with patch('builtins.print') as mock_print:
        command_handler = MagicMock()
        menu_command = MenuCommand(command_handler)
        menu_command.execute(['test_mode'])
        mock_print.assert_called_once_with("MenuCommand output")

@pytest.mark.parametrize('command, args, expected_output', [
    ('menu', ['test_mode'], "MenuCommand output"),
    ('calc', ['2+2'], "CalcCommand output"),
    ('greet', [], "GreetCommand output"),
    ('calchistory', [], "HistoryCommand output"),
    ('historyrepl', [], "HistoryReplCommand output"),
])
def test_main_execute_commands(command, args, expected_output):
    """
    Test executing commands in CalculatorREPL.
    """
    with patch('main.CommandHandler') as mock_command_handler, \
         patch('main.input', side_effect=[f'{command} {" ".join(args)}', 'exit']), \
         patch('builtins.print') as mock_print:
        mock_command_handler.return_value.execute_command.side_effect = lambda cmd, _: print(expected_output) if cmd == command else None
        repl = CalculatorREPL()
        repl.start()
        mock_print.assert_any_call(expected_output)
