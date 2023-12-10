import logging
import coloredlogs


class Log(object):
    logger_instance = None
    c_logger: logging.Logger = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.logger_instance = super(Logger, cls).__new__(cls)
        return cls.logger_instance

    @staticmethod
    def setup_logger():
        Log.c_logger = logging.getLogger(__name__)
        coloredlogs.install(level='DEBUG')

    @staticmethod
    def debug_log(message: str):
        Log.c_logger.debug(message)

    @staticmethod
    def info_log(message: str):
        Log.c_logger.info(message)

    @staticmethod
    def warning_log(message: str):
        Log.c_logger.warning(message)

    @staticmethod
    def error_log(message: str):
        Log.c_logger.error(message)


