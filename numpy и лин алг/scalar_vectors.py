import numpy as np

a = np.random.sample((1, 3))
a = list(a)[0]
b = np.random.sample((1, 3))
b = list(b)[0]
print(a, b)

def scalar_product(a,b):
    s = 0
    for i, j in zip(a, b):
        s += i * j
    return s

def np_scalar_product(a,b):
    return np.array(a).dot(np.array(b))

product_1 = scalar_product(a,b)
product_2 = np_scalar_product(a,b)
# проверим корректность:
print(np.abs(product_1 - product_2).sum())