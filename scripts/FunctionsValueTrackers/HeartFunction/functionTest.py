import numpy as np

def heartFunction(x, k):
    f1 = np.cbrt(x)**2
    f2 = 0.9 * ((3.3 - x ** 2) ** (1 / 2))
    f3 = np.sin(np.pi * x * k)
    return f1 + f2 * f3

print(heartFunction(-1.5, 6.5))
