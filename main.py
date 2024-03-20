# main.py
import sys
from app import App    
from calculation_history import CalculationHistory

# You must put this in your main.py because this forces the program to start when you run it from the command line.
if __name__ == "__main__":
    app = App().start()  # Instantiate an instance of App

def main(args=None):
    if args is None:
        args = sys.argv
