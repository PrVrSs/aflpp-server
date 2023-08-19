import logging
import sys

from loguru import logger as _logger


def setup_logger(cmd_lvl: int = logging.INFO, file_lvl: int = logging.DEBUG):
    _logger.remove()
    _logger.add(sys.stderr, level=cmd_lvl)
    _logger.add('log.txt', level=file_lvl)
    return _logger


logger = setup_logger()
