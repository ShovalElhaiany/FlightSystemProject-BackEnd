import logging

logger = logging.getLogger(__name__)

f_handler = logging.FileHandler('log/log.log')
s_handler = logging.StreamHandler()

f_handler.setLevel(logging.ERROR)
s_handler.setLevel(logging.ERROR)

f_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
s_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

f_handler.setFormatter(f_formatter)
s_handler.setFormatter(s_formatter)

logger.addHandler(f_handler)
logger.addHandler(s_handler)