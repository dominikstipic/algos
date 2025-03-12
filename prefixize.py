from functools import reduce


def get_prefix(s1, s2):
    result = ""
    for k in range(min(len(s1), len(s2))):
        if s1[k] == s2[k]:
            result += s1[k]
        else:
            break
    return result

def prefixize(strs):
    prefixes = []
    for i in range(len(strs)):
        for j in range(i+1, len(strs)):
            s1 = strs[i]
            s2 = strs[j]
            prefix = get_prefix(s1, s2)
            prefixes.append(str(prefix))
    return prefixes

xs = ["aac","aaacab","aa","aaabba","aa"]
xs = prefixize(xs)
xs = reduce(lambda x,y : get_prefix(x, y), xs)
print(xs)