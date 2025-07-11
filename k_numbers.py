import numpy as np

def get_array(start, size, k):
    end = start + size
    numbers = list(range(start, end))
    idxs = np.random.randint(low=0, high=len(numbers), size=k)
    result = np.delete(numbers, idxs)
    return result

start = np.random.randint(100)
size = 100
xs = get_array(start, size, k=4)


for x in xs:
    if x != start:
        print(x)
        start = x
    start += 1




