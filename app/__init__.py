import pkgutil
import importlib
from app.commands import CommandHandler
from app.commands import Command
from app.plugins.menu import MenuCommand
from calculation_history import CalculationHistory
from app.plugins.calchistory import HistoryCommand
from app.plugins.calc import CalcCommand
from app.plugins.historyrepl import HistoryReplCommand

from decimal import Decimal, InvalidOperation
class App:
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()
        self.calculation_history = CalculationHistory()

    def load_plugins(self):
        # Dynamically load all plugins in the plugins directory
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:  # Ensure it's a package
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, Command) and item != Command:  # Check if it's a subclass of Command and not Command itself
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue  # If item is not a class or unrelated class, just ignore
