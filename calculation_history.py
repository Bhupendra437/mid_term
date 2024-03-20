# calculation_history.py

import pandas as pd
import os

class CalculationHistory:
    def __init__(self, filename='calculation_history.csv'):
        self.filename = filename
        self.load_history()

    def load_history(self):
        if os.path.exists(self.filename):
            self.history = pd.read_csv(self.filename)
        else:
            self.history = pd.DataFrame(columns=['Expression', 'Result'])

    def save_history(self):
        self.history.to_csv(self.filename, index=False)

    def add_record(self, expression, result):
        new_record = pd.DataFrame({'Expression': [expression], 'Result': [result]})
        self.history = pd.concat([self.history, new_record], ignore_index=True)

    def clear_history(self):
        self.history = pd.DataFrame(columns=['Expression', 'Result'])

    def delete_history(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
            self.clear_history()

    def view_history(self):
        return self.history
