import os
import logging.config

def update_logging_config():
    # Read environment variables
    log_level = os.getenv('LOG_LEVEL', 'DEBUG').upper()
    log_file = os.getenv('LOG_FILE', 'logs/app.log')

    # Update logging.conf content
    with open('logging.conf', 'r') as file:
        config = file.read()

    config = config.replace('level=DEBUG', f'level={log_level}')
    config = config.replace('args=(\'logs/app.log\', \'a\')', f'args=(\'{log_file}\', \'a\')')

    # Write the updated configuration back to logging.conf
    with open('logging.conf', 'w') as file:
        file.write(config)

if __name__ == '__main__':
    update_logging_config()
    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger(__name__)

    # Example usage
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')
