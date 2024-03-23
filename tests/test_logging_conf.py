# test_logging_config.py
"""
Test suite for the logging configuration.
"""

import logging
import logging.config
import os

def test_logging_configuration():
    """
    Test if the logging configuration is set up correctly.
    """
    # Load the logging configuration
    logging.config.fileConfig('logging.conf')

    # Get the root logger
    logger = logging.getLogger()

    # Check the log level
    assert logger.level == logging.DEBUG  # Replace with the appropriate level

    # Check if the file handler is added
    file_handler_found = False
    for handler in logger.handlers:
        if isinstance(handler, logging.FileHandler):
            file_handler_found = True
            assert handler.level == logging.DEBUG
            # Check the formatter's format string using a dummy record
            dummy_record = logging.LogRecord(name='dummy', level=logging.DEBUG, pathname='', lineno=0, msg='Test message', args=(), exc_info=None)
            formatted_message = handler.formatter.format(dummy_record)
            assert 'DEBUG' in formatted_message
            assert 'Test message' in formatted_message
            assert handler.formatter.datefmt == '%Y-%m-%d %H:%M:%S'
            assert handler.baseFilename.endswith('logs/app.log')
            break

    assert file_handler_found

    # Clean up: remove the log file
    os.remove('logs/app.log')
