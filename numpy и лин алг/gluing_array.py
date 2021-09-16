import numpy as np


def transform(X, a=1):
    Y = X.copy()
    Y[:, 1::2] = a
    Y[:, ::2] **= 3
    return np.concatenate((X, Y[:, ::-1]), axis=-1)


print(transform(np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])))
