# app/plugins/calc/history_command.py

from app.commands import Command

class HistoryCommand(Command):
    def __init__(self, calculation_history):
        self.calculation_history = calculation_history

    def execute(self, args):
        history_df = self.calculation_history.view_history()
        if not history_df.empty:
            for index, row in history_df.iterrows():
                print(f"{row['Expression']} = {row['Result']}")
        else:
            print("No history available.")
