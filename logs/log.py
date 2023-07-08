import os
import logging
from logging.handlers import RotatingFileHandler

LOG_LEVELS = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
LOG_FORMAT = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
MAX_BYTES = 3000
BACKUP_COUNT = 2


def create_logger():
    log_dir = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    for level in LOG_LEVELS:
        level_dir = os.path.join(log_dir, level)
        os.makedirs(level_dir, exist_ok=True)
        log_file = os.path.join(level_dir, f'{level}.log')

        file_handler = RotatingFileHandler(log_file, maxBytes=MAX_BYTES, backupCount=BACKUP_COUNT)
        file_handler.setLevel(level)
        file_handler.setFormatter(LOG_FORMAT)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_handler.setFormatter(LOG_FORMAT)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
