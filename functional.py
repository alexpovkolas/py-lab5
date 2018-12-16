from collections.abc import Iterable


def counter(func):
    def wrapper(*args, **kwargs):
        wrapper._calls += 1
        func(*args, **kwargs)
        return wrapper._calls

    wrapper._calls = 0
    return wrapper


@counter
def smart_function():
    print("Smart function call")


def flatten(it):
    for i in it:
        if isinstance(i, Iterable) and not isinstance(i, str):
            yield from flatten(i)
        else:
            yield i
