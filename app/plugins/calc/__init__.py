import sys
import argparse
from app.plugins.calc.calculator import Calculator
from decimal import Decimal, InvalidOperation
from app.commands import Command
from app.plugins.calc.calculator.history import add_to_history, get_history

class HistoryCommand(Command):
    name = 'calchistory'

    def __init__(self, calculation_history):
        self.calculation_history = calculation_history

    def execute(self, args):
        history_df = self.calculation_history.view_history()
        if not history_df.empty:
            for index, row in history_df.iterrows():
                print(f"{row['Expression']} = {row['Result']}")
        else:
            print("No history available.")

class CalcCommand(Command):
    name = 'calc'

    def __init__(self, calculation_history):
        self.calculation_history = calculation_history

    def execute(self, args):
        if len(args) != 3:
            print("Usage: calc <number1> <number2> <operation>")
            return

        a, b, operation = args
        self.calculate_and_print(a, b, operation)

    def calculate_and_print(self, a, b, operation_name):
        operation_mappings = {
            'add': Calculator.add,
            'subtract': Calculator.subtract,
            'multiply': Calculator.multiply,
            'divide': Calculator.divide
        }

        try:
            a_decimal, b_decimal = map(Decimal, [a, b])
            operation_function = operation_mappings.get(operation_name)
            if operation_function:
                result = operation_function(a_decimal, b_decimal)
                print(f"The result of {a} {operation_name} {b} is equal to {result}")
                expression = f"{a} {operation_name} {b}"
                self.calculation_history.add_record(expression, result)
                self.calculation_history.save_history()
            else:
                print(f"Unknown operation: {operation_name}")
        except InvalidOperation:
            print(f"Invalid number input: {a} or {b} is not a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")
