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


for real_call_count in range(1, 5):
    assert smart_function() == real_call_count

expected = [1, 2, 0, 1, 1, 2, 1, 'ab']
actual = flatten([1, 2, range(2), [[], [1], [[2]]], (x for x in [1]), 'ab'])
assert expected == list(actual)
