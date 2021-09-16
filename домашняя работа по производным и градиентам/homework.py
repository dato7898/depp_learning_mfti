import numpy as np

x = 0
d = 0.000001

def derivative(F, x):
    return (F(x + d) - F(x)) / d

def F(x):
    return x**x

print(derivative(F, np.e))

def F(x):
    return np.tan(x) * np.log(np.cos(x**2) + 1)

print(derivative(F, x))

def F(x):
    return np.abs(x)**2

print(derivative(F, x))

def F(x):
    return np.abs(x)**2

print(derivative(F, x))

def F(x):
    return np.sin(x) / x

print(derivative(F, x))

def F(x):
    if x == 0:
        return 0
    else:
        return x**2

print(derivative(F, x))