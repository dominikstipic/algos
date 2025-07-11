from typing import List
import numpy as np
from manhatton import manhatton_set

def get_words():
    with open("word.txt", "r") as fp:
        X = fp.readlines()
        X = [X.strip() for X in X]
    return X

def trajectory(start, end) -> List[str]:
    pass

def prefixes_all(w_target, words):
    result = []
    for w in words:
        if w.startswith(w_target):
            result.append(w)
    return result

def prefixes(w_target, words, k):
    ps = prefixes_all(w_target, words)
    ps = [p for p in ps if len(p) == (len(w_target)+k)]
    return ps

def prefixes(w_target, words, k):
    ps = prefixes_all(w_target, words)
    ps = [p for p in ps if len(p) == (len(w_target)+k)]
    return ps

def fill(s, k):
    result = s
    x = result[-1]
    while len(result) != (len(s) + k):
        result += x
    return result

def index_of(s, X):
    """
        Return the index of element in the matrix. 
    """
    for i, xs in enumerate(X):
        for j, x in enumerate(xs):
            if x == s:
                return j,i
    return "¤"

start = "sun"
target = "water"
ws = get_words()
ps = prefixes(start, ws, k=2)
print(ps[0])
ms = manhatton_set(ps[0], k=1)
print(ms)

