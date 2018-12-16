import functools


def transpose(it):
    return zip(*it)


def _multiply(first, second):
    _first = int(first) if isinstance(first, str) else first
    _second = int(second) if isinstance(second, str) else second
    return _first * _second


def scalar_product(first, second):
    try:
        return sum([_multiply(i, j) for (i, j) in zip(first, second)])
    except:
        return None


expected = [[1, 2], [-1, 3]]
actual = transpose([[1, -1], [2, 3]])
assert expected == list(map(list, actual))


expected = 1
actual = scalar_product([1, '2'], [-1, 1])
assert expected == actual
actual = scalar_product([1, 'abc'], [-1, 1])
assert actual is None
