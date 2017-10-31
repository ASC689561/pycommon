import logging

import functools

import time



def log(logger, level=None, format='%s: %s ms'):
    if level is None:
        level = logging.DEBUG

    def decorator(fn):
        @functools.wraps(fn)
        def inner(*args, **kwargs):
            start = time.time()
            logger.log(level, "start")

            result = fn(*args, **kwargs)

            duration = time.time() - start
            logger.log(level, "end time: {} ".format(duration))
            logger.log(level, format, repr(fn), duration * 1000)
            return result

        return inner

    return decorator
