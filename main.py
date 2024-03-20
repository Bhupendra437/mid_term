import sys
from app import App
from app.commands import CommandHandler
from app.plugins.menu import MenuCommand
from calculation_history import CalculationHistory
from app.plugins.calc.history_command import HistoryCommand
from app.plugins.calc import CalcCommand
from app.plugins.calc.history_repl_command import HistoryReplCommand

class CalculatorREPL:
    def __init__(self):
        self.app = App()
        self.command_handler = CommandHandler()
        self.calculation_history = CalculationHistory()

        # Register core commands
        self.command_handler.register_command("menu", MenuCommand(self.command_handler))
        self.command_handler.register_command("calchistory", HistoryCommand(self.calculation_history))
        self.command_handler.register_command("calc", CalcCommand(self.calculation_history))
        self.command_handler.register_command("historyrepl", HistoryReplCommand(self.calculation_history))

        # Load plugins
        self.app.load_plugins()

    def start(self):
        print("Welcome to the Calculator REPL. Type 'menu' to see available commands, 'exit' to exit.")
        while True:
            user_input = input(">>> ").strip().split()
            if not user_input:
                continue
            command = user_input[0]
            args = user_input[1:]

            if command.lower() == 'exit':
                print("Exiting the Calculator REPL.")
                break
            else:
                self.command_handler.execute_command(command, args)

if __name__ == "__main__":
    repl = CalculatorREPL()
    repl.start()
