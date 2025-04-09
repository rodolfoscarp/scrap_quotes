from loguru import logger


def setup_logs():
    logger.add("logs.log", backtrace=True, level="DEBUG")
