import numpy as np


n = 33
k = 3
F = np.zeros(n)
F[0] = 1
F[1] = 1

for i in range(2, n):
    F[i] = F[i-1] + F[i-2]*k

print(F[-1])