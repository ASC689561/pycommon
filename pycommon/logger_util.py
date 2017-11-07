import logging
import os
from logging.handlers import RotatingFileHandler


class LogBuilder:
    def __init__(self):
        self.handlers = []
        self.format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        pass

    def build(self):
        logging.basicConfig(level=logging.DEBUG, format=self.format, handlers=self.handlers)

    def init_stream_handler(self, *levels):
        for v in levels:
            handler = logging.StreamHandler()
            handler.setLevel(v)
            self.handlers.append(handler)

    def init_file_log(self, log_path):
        if not os.path.exists(log_path):
            os.makedirs(log_path)

        debug_log = RotatingFileHandler(log_path + "/debug.log", maxBytes=5 * 1024 * 1024, mode='a', backupCount=10)
        debug_log.setLevel(logging.DEBUG)

        info_log = RotatingFileHandler(log_path + "/info.log", maxBytes=5 * 1024 * 1024, mode='a', backupCount=10)
        info_log.setLevel(logging.INFO)

        error_log = RotatingFileHandler(log_path + "/error.log", maxBytes=5 * 1024 * 1024, mode='a', backupCount=10)
        error_log.setLevel(logging.ERROR)

        self.handlers.extend([debug_log, info_log, error_log])
