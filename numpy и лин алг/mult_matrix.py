import numpy as np

a = [[1, 2, 3],
     [1, 2, 3],
     [1, 2, 3]]
b = [[1, 2, 3],
     [1, 2, 3],
     [1, 2, 3]]
c = [[1, 2, 3]]
d = [[1],
     [2],
     [3]]

print(np.dot(a, b))
print(np.dot(c, d))


def my_dot(a, b):
    res = [[0 for _ in range(len(a))] for _ in range(len(b[0]))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                res[i][j] += a[i][k] * b[k][j]
    return res


print(my_dot(a, b))
print(my_dot(c, d))
