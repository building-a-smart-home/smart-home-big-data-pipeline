import logging
from .config import LOG_FILE

def logger():
    logging.basicConfig(
        format='%(asctime)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename=LOG_FILE,
        filemode='w'
    )
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    return logger
