import numpy as np

a = np.array([
    [5,10,15],
    [20,10,11],
    [6,10,15]
])
a.sum(axis=1)
print(a.dtype)