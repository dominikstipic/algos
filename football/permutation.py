"""
    Modules for calculating the probability of events.
"""

def _insert_list(xs: list, i: int, h: int) -> list:
    ys = xs.copy()
    ys.insert(i, h)
    return ys

def insert(h: int, xs: list) -> list:
    result = []
    for i in range(len(xs)+1):
        ys = _insert_list(xs, i, h)
        result.append(ys)
    return result

def exchange(xs: list, i: int, j: int) -> list:
    a,b = xs[i], xs[j]
    xs[j] = a
    xs[i] = b
    return xs

def permute_list(xs: list) -> list:
    if len(xs) == 2:
        a,b = xs
        return [[a,b], [b,a]]
    result = []
    for i in range(len(xs)):
        h = xs[i]
        xs = exchange(xs, 0, i)
        yss = permute_list(xs[1:])
        for ys in yss:
            result.append([h] + ys)
    return result

def permutation(n: int) -> int:
    S = 1
    for i in range(2, n+1):
        S = S*i
    return S

xs = list(range(1,9))
