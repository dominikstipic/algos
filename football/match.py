import permutation as perm

"""
    Module tests the calculation of the 
"""


def test_paper():
    p4 = perm.permutation(4)
    p8 = perm.permutation(8)
    result = (p4*p4)/p8
    
    N, M = 8, 4
    xs = list(range(1,N+1))
    total = perm.permutation(len(xs))
    pss = perm.permute_list(xs)
    k = 0
    target = set(list(range(1, M+1)))
    for ps in pss:
        group = set(ps[:M])
        if target == group:
            k+=1
    print(f"Probability = {round(result * 100, 3)} %")
    assert result == k/total



N = 32
M = 4
p4 = perm.permutation(M)
p28 = perm.permutation(N-M)
p32 = perm.permutation(N)
result = (p4*p28)/p32
print(f"Probability = {result * (10**6)} %")