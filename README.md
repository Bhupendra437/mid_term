**Use of Design patterns-**
1. **Consistent Structure**: With each plugin having its own directory. This consistency helps with maintainability and understanding the project layout.

2. **DRY Principle (Don't Repeat Yourself)**: The code avoids unnecessary repetition and duplication. For example, in the `CalcCommand` and `HistoryCommand` classes, specific functionalities are encapsulated within methods, and I’ve avoided repeating logic across different parts of the code.

3. **Single Responsibility Principle (SRP)**: Each class in the codebase has a single responsibility. For example, `CalcCommand` is responsible for performing calculations, `HistoryCommand` manages the calculation history, and `HistoryReplCommand` provides an interactive REPL for history management.

4. **Open/Closed Principle (OCP)**: Classes are open for extension but closed for modification. For instance, adding a new command or a new operation to the calculator can be done by extending existing classes or adding new entries to dictionaries without modifying existing code.

5. **Liskov Substitution Principle (LSP)**: Command classes (`CalcCommand`, `HistoryCommand`, `HistoryReplCommand`) adhere to the `Command` interface by implementing the `execute` method. This ensures that they can be used interchangeably wherever a `Command` is expected.

6. **Dependency Inversion Principle (DIP)**: The code depends on abstractions rather than concrete implementations. For example, command classes depend on the abstract `Command` class, and the `App` class depends on the abstract `CommandHandler` for registering and executing commands.

7. **Separation of Concerns**: The code separates concerns well. The `App` class handles the overall application setup and plugin loading, command classes handle specific user commands, and the `Calculator` class deals with arithmetic operations.

8. **Facade Pattern and Command Pattern**: The code offers a simplified interface using REPL for complex Pandas data manipulations for effective calculation and history management using commands.

Overall, the use of design principles helps with well-structured and maintainable codebase. 


**Use of environment variables-**

I've used environment variables to configure certain aspects of the application, specifically the logging configuration. Here's how I've done it:
Loading Environment Variables: At the beginning of main.py, load_dotenv() function is used from the ‘dotenv’ package to load environment variables from a .env file into application's environment.
Accessing Environment Variables: These environment variables were accessed using os.getenv(). For example, retrieved the application environment and logging level from the environment variables APP_ENV and LOG_LEVEL, respectively.
https://github.com/Bhupendra437/mid_term/blob/main/main.py
By using environment variables in this way, the application is made more flexible and easier to configure in different environments (e.g., development, testing, production) without needing to change the code itself. 


**Use of logging-**
In this application, logging is used to record various events that occur during the execution of the program. Here's how you I am using logging in the application:
1.	Importing the logging module: At the beginning of main.py file, I imported the logging module and other necessary modules for logging configuration.
2.	Loading the logging configuration: I used the fileConfig function from the logging.config module to load the logging configuration from the logging.conf file.
3.	Creating a logger: A logger instance is created using the getLogger function.
4.	Using the logger: Throughout your main.py file, the logger is used to log messages at different levels. For example, logger.debug is used to log debugging information, logger.info to log informational messages, and logger.error to log error messages.
5.	Logging configuration file (logging.conf): This file defines the structure and behavior of loggers, handlers, and formatters. It specifies that log messages should be written to a file (logs/app.log) and formatted with a timestamp, log level, and message.
6.	Dynamic logging- The logging level can be adjusted dynamically through environment variables as well as logging.conf to control the verbosity of the log output.
Use of logging can record detailed information about application operation, which is invaluable for debugging and monitoring the application's behavior. The log messages are written to a file, making it easy to review them later.

https://github.com/Bhupendra437/mid_term/blob/main/logging.conf
https://github.com/Bhupendra437/mid_term/blob/main/main.py


**"Look Before You Leap" (LBYL) and "Easier to Ask for Forgiveness than Permission" (EAFP)-**
**EAFP-**
This approach is used in the execute_command method of the CommandHandler class. Instead of checking if the command exists in the commands dictionary before attempting to execute it (LBYL), I directly try to execute the command and catch the KeyError exception if the command does not exist.
**Example-**
https://github.com/Bhupendra437/mid_term/blob/main/app/commands/__init__.py

**code snippet-**

![image](https://github.com/Bhupendra437/mid_term/assets/157599950/2530dc83-3ad1-4d8a-9790-055900bd07e8)


In this code, the try block attempts to execute the command. If the command is not found in the commands dictionary, a KeyError is raised, which is then caught by the except block. This block handles the error by printing an error message and logging the error.


