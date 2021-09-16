import numpy as np


def cumsum(A):
    return np.cumsum(A, axis=1)


print(cumsum(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])))
