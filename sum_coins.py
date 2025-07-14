import numpy as np

def coin_sum(elements, target):
    elements = np.array([1,3,5])
    result = np.array([0,0,0])

    L = len(elements)
    for i in range(1, L+1):
        if(target <= 0 or elements[-i] > target):
            break
        k = int(target / elements[-i])
        e = elements[-i]
        x = k*e
        target -= x
        result[-i] = k
        
    if(target > 0):
        return None
    else:
        return result

coins = [1,3,5]
target = 15
xs = coin_sum(coins, target)
print(xs)