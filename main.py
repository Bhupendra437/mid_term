import os
import logging
from logging.config import fileConfig
from app import App
from app.commands import CommandHandler
from app.plugins.menu import MenuCommand
from app.plugins.greet import GreetCommand
from calculation_history import CalculationHistory
from app.plugins.calchistory import HistoryCommand
from app.plugins.calc import CalcCommand
from app.plugins.historyrepl import HistoryReplCommand
from dotenv import load_dotenv

def update_logging_config():
    # Read environment variables
    log_level = os.getenv('LOG_LEVEL', 'DEBUG').upper()
    log_file = os.getenv('LOG_FILE', 'logs/app.log')

    # Ensure the directory for the log file exists
    log_dir = os.path.dirname(log_file)
    os.makedirs(log_dir, exist_ok=True)

    # Update logging.conf content
    with open('logging.conf', 'r') as file:
        config = file.read()

    config = config.replace('level=DEBUG', f'level={log_level}')
    config = config.replace('args=(\'logs/app.log\', \'a\')', f'args=(\'{log_file}\', \'a\')')

    # Write the updated configuration back to logging.conf
    with open('logging.conf', 'w') as file:
        file.write(config)

# Load environment variables from .env file
load_dotenv()

# Update logging configuration based on environment variables
update_logging_config()

# Load the updated logging configuration
fileConfig('logging.conf')

# Get a logger for this module
logger = logging.getLogger(__name__)
logger.propagate = True

class CalculatorREPL:
    def __init__(self):
        logger.debug("Initializing CalculatorREPL")
        self.app = App()
        self.command_handler = CommandHandler()
        self.calculation_history = CalculationHistory()

        # Register core commands
        logger.debug("Registering core commands")
        self.command_handler.register_command("menu", MenuCommand(self.command_handler))
        self.command_handler.register_command("calc", CalcCommand(self.calculation_history))
        self.command_handler.register_command("greet", GreetCommand())
        self.command_handler.register_command("calchistory", HistoryCommand(self.calculation_history))
        self.command_handler.register_command("historyrepl", HistoryReplCommand(self.calculation_history))

        # Load plugins
        logger.debug("Loading plugins")
        self.app.load_plugins()

    def start(self):
        logger.info("Starting the Calculator REPL.")
        print("Welcome to the Calculator REPL. Type 'menu' to see available commands, 'exit' to exit.")
        while True:
            user_input = input(">>> ").strip().split()
            if not user_input:
                continue
            command = user_input[0]
            args = user_input[1:]

            logger.debug("Received command: %s with args: %s", command, args)

            if command.lower() == 'exit':
                logger.info("Exiting the Calculator REPL.")
                print("Exiting the Calculator REPL.")
                break
            else:
                try:
                    logger.info("Executing command: %s", command)
                    self.command_handler.execute_command(command, args)
                except Exception as e:
                    logger.error("An error occurred while executing command '%s': %s", command, e)

if __name__ == "__main__":
    repl = CalculatorREPL()
    repl.start()
