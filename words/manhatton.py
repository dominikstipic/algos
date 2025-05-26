import numpy as np
from collections import Counter
from pynput import keyboard
import string

def get_keyboard() -> np.array:
     return np.array([
        ['Q', 'W', 'E', 'R', 'T', 'Z', 'U', 'I', 'O', 'P', 'Š', 'Đ'],
        ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Č', 'Ć', 'Ž'],
        ["<", 'Y', 'X', 'C', 'V', 'B', 'N', 'M', ";", ".", "-", "+"]])

def get_alphabet() -> np.array:
    return string.ascii_letters[0:26]

def index_of(s, X):
    """
        Return the index of element in the matrix. 
    """
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

def manhatton_set(string: str, k: int):
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

def words():
    """
        All the words which appear on the Linux system. 
    """
    with open("word.txt", "r") as fp:
        X = fp.readlines()
        X = [X.strip() for X in X]
    return X

def manhaton_distance(start: str, end: str):
    result = {}
    a = dict(Counter(start))
    b = dict(Counter(end))

    aib = set(a).intersection(set(b))
    aib = set(a).difference(set(b))

def manhattan_distance(s1: str, s2: str, vocabulary: np.array) -> int:
    """
        Manhattan distance between the two words from the vocabulary. 
    """
    result = 0
    n1, n2 = len(s1), len(s2)
    if n1 > n2:
        s2 = fill(s2, n1 - n2)
    elif n2 > n1:
        s1 = fill(s1, n2 - n1)
    N = len(s1)
    for i in range(N):
        l1, l2 = s1[i], s2[i]
        x1, y1 = index_of(l1.upper(), vocabulary)
        x2, y2 = index_of(l2.upper(), vocabulary)
        dx = abs(x2-x1)
        dy = abs(y2-y1)
        delta = dx+dy
        result += delta
    return result

def on_press(key: str):
    try:
        print(f'Key {key.char} pressed')
    except AttributeError:
        print(f'Special key {key} pressed')

def alphabetical_difference(word1: str, word2: str) -> int:
    letter_diff = lambda a,b : abs(ord(a) - ord(b))
    if(len(word1) == len(word2)):
        total = 0
        for w1,w2 in zip(word1, word2):
            total += letter_diff(w1, w2)
        return total
    
def number_difference(word1: str, word2: str) -> int:
    if(len(word1) == len(word2)):
        total = 0
        for w1,w2 in zip(word1, word2):
            if(w1!=w2):
                total += 1
        return total

def preffix_set(preffix: str, words: list) -> list:
    """
        The list of words which start with prefix. 
    """
    result = []
    for w in words:
        if w.startswith(preffix):
            result.append(w)
    return result

def neighborhood(a: str) -> tuple:
    """
        Return the alphabetical neighbourhood of the given letter 
    """
    alpha = get_alphabet()
    if a == "a":
        return "z", "b"
    elif a == "z":
        return "y", "a"
    else:
        idx = ord(a) - ord("a")
        return alpha[idx-1], alpha[idx+1]

def change(words: str, idx: int, letter: str) -> str: 
    """
        Change the letter of the word on specific index. 
    """
    xs = list(words)
    xs[idx] = letter
    return "".join(xs)

def preffix_similar_set(preffix: str, words: list) -> list:
    """
        The list of words which start with prefix. 
    """
    preffix = preffix.lower()
    recommendation = preffix_set(preffix, words)
    if not recommendation:
        ds = {} # 0 -> (set_min, set_plus)
        for i in range(len(preffix)): 
            w_plus, w_min = neighborhood(preffix[i])
            w_plus_word, w_min_word = change(preffix, i, w_plus), change(preffix, i, w_min)
            w_plus_set, w_min_set = preffix_set(w_plus_word, words),  preffix_set(w_min_word, words)
            if(len(w_plus_set) == 0 and len(w_min_set) == 0):
                continue
            else:
                ds[(w_plus, w_min)] = w_plus_set, w_min_set
        return ds
    else: 
        return recommendation

ws = words()
start = "anti"
xs = preffix_similar_set("amti", ws)
print(xs)