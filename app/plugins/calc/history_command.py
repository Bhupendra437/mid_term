# app/plugins/calc/history_command.py

from app.commands import Command
from app.plugins.calc.calculator.history import get_history

class HistoryCommand(Command):
    def execute(self, args):
        history = get_history()
        if history:
            for entry in history:
                print(f"{entry['expression']} = {entry['result']}")
        else:
            print("No history available.")
