import re
import numpy as np

def from_letter2binary(letter):
    let2bin = {
        "a": "1010",
        "b": "1011",
        "c": "1100",
        "d": "1101",
        "e": "1110",
        "f": "1111",
    }
    nums = let2bin[letter]
    fun = lambda x : True if x == "1" else False
    return [fun(x) for x in nums]

def from_num2binary(num):
    result = []
    for i in reversed(range(4)):
        k = 2**i
        if num - k >= 0:
            result.append(True)
            num -= k 
        else:
            result.append(False)
    return np.array(result)

def from_hex2bin(string):
    bs  = bytes(string, "utf-8")
    hs = bs.hex()
    result = np.array([])
    for h in hs:
        if re.match("[0-9]+", h):
            bools = from_num2binary(int(h))
            result = np.append(result, bools)
        else:
            ones_zeros = from_letter2binary(h)
            result = np.append(result, ones_zeros)
    return np.array(result)

def from_bin2hex(result: list):
    x = 0
    result = reversed(result)
    for i, r in enumerate(result):
        if r == True:
            x += 2**i
    return hex(x)

a = from_hex2bin("ig")
b = from_hex2bin("0e")
z = np.logical_or(a,b)
from_bin2hex(z)
