import functools
import logging

import time


def custom_timing_log(func, name=None):
    def timing(f):
        def wrap(*args):
            time1 = time.time()
            ret = f(*args)
            time2 = time.time()
            log_time = (time2 - time1) * 1000.0
            if name is None:
                func(f.__name__, log_time)
            else:
                func(name, log_time)
            return ret

        return wrap

    return timing


def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        log_time = (time2 - time1) * 1000.0
        logging.log(60, '%s function took %0.3f ms' % (f.__name__, log_time), extra={f.__name__: str(log_time)})

        return ret

    return wrap


def before(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        self = args[0]
        func(*args, **kwargs)
        return self

    return wrapped


def ignore_exception(time=3):
    def f_method(func):
        @functools.wraps(func)
        def ignore(*args, **kw):
            for v in range(0, time):
                try:
                    result = func(*args, **kw)
                    return result
                except Exception as ex:
                    if v == time - 1:
                        raise ex

        return ignore

    return f_method
