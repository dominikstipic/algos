import numpy as np
import functools
"""
K numbers bigger then 50 which divide the X. 
Decompose the number into primes. 
Sieve of Eratosthenes: generator which spits the primes.  
"""

def eratosthenes(start=2, end=np.inf):
    current = 2
    while(True):
        is_prime = True
        for i in range(start, current):
            if current % i == 0:
                is_prime = False
                break
        if is_prime:
            yield current
        current += 1
        if(current > end):
            break

def _prime_max_factorization(x, prime):
    """
        We putted private variable prefix _ in order to denote that function is called from public method prime_decompose and it is 
        not advised to call it independently. In opposite scenario, one shoud check arguments, i.o.w that prime is actually prime number.
        We expect that caller is always calling the function with primes. We also expect that prime divides x. 
    """
    k = 0
    while(x >= 1):
        x = x / prime
        k += 1
    return k-1

def _grid_search2d(x, y):
    result = []
    for i in range(1, x+1):
        for j in range(1, y+1):
            result.append((i,j))
    return result

def _grid_search_expand(grid, p):
    result = []
    for i in range(len(grid)):
        row = grid[i]
        for pi in range(1, p+1):
            row_new = (*row, pi)
            result.append(row_new)
    return result

def grid_search(xs):
    assert len(xs) >= 2, "Grid search can only be performed for dimensions greater then 2"
    G = _grid_search2d(xs[0], xs[1])
    for i in range(2, len(xs)):
        G = _grid_search_expand(G, xs[i])
    return G

def grid_search_generator(xs):
    assert len(xs) >= 2, "Grid search can only be performed for dimensions greater then 2"
    G = grid_search(xs)
    for row in G:
        yield np.array(row)

def mul(xs):
    return functools.reduce(lambda x,y : x*y, xs, 1)

def prime_decompose(x):
    primes = [k for k in eratosthenes(end=x) if x % k == 0]
    max_exponents = [_prime_max_factorization(x, p) for p in primes]
    cond = lambda primes, row : mul(primes**row) == x
    for row in grid_search_generator(max_exponents):
        if cond(primes, row):
            return np.array(primes), row
    return [], []

x = 4332
xs, ys = prime_decompose(x)
print(xs, ys, mul(xs**ys))