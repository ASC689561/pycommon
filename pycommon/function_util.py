import functools


def fluent(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        self = args[0]
        func(*args, **kwargs)
        return self

    return wrapped