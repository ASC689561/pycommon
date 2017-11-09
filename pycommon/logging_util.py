import logging
import os
from logging.handlers import RotatingFileHandler

from logstash import TCPLogstashHandler


class LogBuilder:
    def __init__(self):
        self.handlers = []
        self.format_str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

    def build(self):
        logging.basicConfig(level=logging.DEBUG, format=self.format_str, handlers=self.handlers)

    def set_format(self, format_str):
        self.format_str = format_str
        return self

    def init_stream_handler(self):
        self.handlers.append(logging.StreamHandler())
        return self

    def init_rotating_file(self, log_path):
        if not os.path.exists(log_path):
            os.makedirs(log_path)

        debug_log = RotatingFileHandler(log_path + "/debug.log", maxBytes=5 * 1024 * 1024, mode='a', backupCount=10)
        debug_log.setLevel(logging.DEBUG)

        info_log = RotatingFileHandler(log_path + "/info.log", maxBytes=5 * 1024 * 1024, mode='a', backupCount=10)
        info_log.setLevel(logging.INFO)

        error_log = RotatingFileHandler(log_path + "/error.log", maxBytes=5 * 1024 * 1024, mode='a', backupCount=10)
        error_log.setLevel(logging.ERROR)

        self.handlers.extend([debug_log, info_log, error_log])
        return self

    def init_logstash(self, host, port, *levels):
        for v in levels:
            logstash_handler = TCPLogstashHandler(host, port, version=1)
            logstash_handler.setLevel(v)
            self.handlers.append(logstash_handler)

        return self
