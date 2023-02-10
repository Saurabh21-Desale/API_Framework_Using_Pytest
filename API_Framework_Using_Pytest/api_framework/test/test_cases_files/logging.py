import logging.config
import pytest

logging.config.fileConfig('logger.ini', disable_existing_loggers=False)
logger = logging.getLogger('Logger')

def test_hello():
    logger.info("Hi")