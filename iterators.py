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


