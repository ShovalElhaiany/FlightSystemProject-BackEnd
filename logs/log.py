import logging
import os
from logging.handlers import RotatingFileHandler

LOGGER_LEVEL = logging.DEBUG
LOG_LEVELS = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
LOG_FORMAT = logging.Formatter("time: %(asctime)s - file: %(filename)s - level: %(levelname)s - message: {e}'%(message)s")
MAX_BYTES = 3000
BACKUP_COUNT = 2

def create_logger():
    """
    Create a logger object with file and console handlers for each log level directory.

    Returns:
        logging.Logger: The logger object.
    """
    log_dir = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger(__name__)
    logger.setLevel(LOGGER_LEVEL)

    for level in LOG_LEVELS:
        level_dir = os.path.join(log_dir, level)
        os.makedirs(level_dir, exist_ok=True)
        log_file = os.path.join(level_dir, f'{level}.log')

        file_handler = RotatingFileHandler(log_file, maxBytes=MAX_BYTES, backupCount=BACKUP_COUNT)
        file_handler.setLevel(level)
        file_handler.setFormatter(LOG_FORMAT)
        logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(LOG_FORMAT)
    logger.addHandler(console_handler)


    return logger


logger = create_logger()

def log_and_raise(exception, level):
    """
    Log an exception and raise it with the specified log level.

    Args:
        exception (Exception): The exception to be logged and raised.
        level (str): The log level for the exception.

    Raises:
        Exception: The original exception is raised after logging.
    """
    error_msg = exception
    
    if level == 'debug':
        logger.debug(error_msg)
    if level == 'info':
        logger.info(error_msg)
    if level == 'warning':
        logger.warning(error_msg)
    if level == 'error':
        logger.error(error_msg)
    if level == 'critical':
        logger.critical(error_msg)

    raise error_msg
