import numpy as np
import itertools


def encode(a):
    return tuple(np.array(z) for z in list(zip(*[(x, len(list(y))) for x, y in itertools.groupby(a)])))


print(encode(np.array([1, 2, 2, 3, 3, 1, 1, 5, 5, 2, 3, 3])))
# [1, 2, 3, 1, 5, 2, 3]
# [1, 2, 2, 2, 2, 1, 2]
