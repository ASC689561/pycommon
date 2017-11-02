import functools


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
