from abc import ABC, abstractmethod
import logging

logger = logging.getLogger('root')

class Command(ABC):
    @abstractmethod
    def execute(self, args):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command, args):
        try:
            self.commands[command].execute(args)
        except KeyError:
            print(f"No such command: {command}")
            logger.error(f"No such command: {command}")
