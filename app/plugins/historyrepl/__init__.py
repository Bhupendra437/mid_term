# app/plugins/calc/history_repl_command.py

from app.commands import Command

class HistoryReplCommand(Command):
    def __init__(self, calculation_history):
        self.calculation_history = calculation_history

    def execute(self, args):
        while True:
            print("\nOptions: load, save, add, clear, delete, view, exit")
            choice = input("Enter your choice: ").strip().lower()

            if choice == 'load':
                self.calculation_history.load_history()
                print("History loaded.")

            elif choice == 'save':
                self.calculation_history.save_history()
                print("History saved.")

            elif choice == 'add':
                expression = input("Enter the expression: ")
                result = input("Enter the result: ")
                self.calculation_history.add_record(expression, result)
                print("Record added.")

            elif choice == 'clear':
                self.calculation_history.clear_history()
                print("History cleared.")

            elif choice == 'delete':
                self.calculation_history.delete_history()
                print("History deleted.")

            elif choice == 'view':
                print(self.calculation_history.view_history())

            elif choice == 'exit':
                break

            else:
                print("Invalid choice. Please try again.")