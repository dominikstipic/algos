xs = list(range(1,9))

def _insert_list(xs, i, h):
    ys = xs.copy()
    ys.insert(i, h)
    return ys

def insert(h, xs):
    result = []
    for i in range(len(xs)+1):
        ys = _insert_list(xs, i, h)
        result.append(ys)
    return result

def exchange(xs, i, j):
    a,b = xs[i], xs[j]
    xs[j] = a
    xs[i] = b
    return xs

def permute(xs: list) -> list:
    if len(xs) == 2:
        a,b = xs
        return [[a,b], [b,a]]
    result = []
    for i in range(len(xs)):
        h = xs[i]
        xs = exchange(xs, 0, i)
        yss = permute(xs[1:])
        for ys in yss:
            result.append([h] + ys)
    return result

xs = ["A", "B", "C", "D", "E"]
rs = permute(xs)
for i, r in enumerate(rs):
    print(i, r)