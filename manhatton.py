import numpy as np

def index_of(s, X):
    for i, xs in enumerate(X):
        for j, x in enumerate(xs):
            if x == s:
                return j,i
    return "¤"

def fill(s, k):
    result = s
    x = result[-1]
    while len(result) != (len(s) + k):
        result += x
    return result

def manhatton_distance(s1: str, s2: str, X: np.array):
    result = 0
    n1, n2 = len(s1), len(s2)
    if n1 > n2:
        s2 = fill(s2, n1 - n2)
    elif n2 > n1:
        s1 = fill(s1, n2 - n1)
    N = len(s1)
    for i in range(N):
        l1, l2 = s1[i], s2[i]
        x1, y1 = index_of(l1.upper(), X)
        x2, y2 = index_of(l2.upper(), X)
        dx = abs(x2-x1)
        dy = abs(y2-y1)
        delta = dx+dy
        result += delta
    return result

def neighbour_index(x: int, y: int, k: int, x_lenght: int, y_length: int):
    xs = [
        (x-k, y),
        (x+k, y),
        (x, y+k),
        (x, y-k)
    ]
    xs = [(x,y) for x,y in xs if (x >= 0 and y>=0)]
    xs = [(x,y) for x,y in xs if (x < x_lenght and y < y_length)]
    return xs

def change_string_elem(string, index, c):
    return string[:index] + c + string[index+1:]

def manhatton_set(string: str, k: int, X: np.array):
    x_length = len(X[0]) 
    y_length = len(X)
    result = set()
    string = string.upper()
    for i, s in enumerate(string):
        x,y = index_of(s, X)
        index_list = neighbour_index(x, y, k, x_length, y_length)
        for x,y in index_list:
            l = X[y, x]
            rs = change_string_elem(string, i, l)
            result.update([rs])
    return result

"---------------------------------------------------"

X = np.array([
        ['Q', 'W', 'E', 'R', 'T', 'Z', 'U', 'I', 'O', 'P', 'Š', 'Đ'],
        ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Č', 'Ć', 'Ž'],
        ["<", 'Y', 'X', 'C', 'V', 'B', 'N', 'M', ";", ".", "-", "+"]
    ])

ms = manhatton_set("far", 1, X)
print(ms)


s1 = "dominik"
s2 = "gominik"
d = manhatton_distance(s1, s2, X)
print(d)