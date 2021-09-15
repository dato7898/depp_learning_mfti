import numpy as np

def diag_2k(a):
    a = np.diagonal(a, offset=0, axis1=0, axis2=1)
    return sum(a[a % 2 == 0])

a = np.random.randint(1, 10, size=(5, 5))
print(a)

print(diag_2k(a))