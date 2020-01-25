import numpy as np


# input
n = 87
m = 16


# init
F = np.zeros(n).astype(np.int64)  # no floats to avoid numerical issues
F[0], F[1] = 1, 1


# dynamic programming
for i in range(2, n):
    
    if i < m:
        # usual fibonnaci
        F[i] = F[i-1] + F[i-2]
    elif i == m:
        # F at (-1) is undefined, hardcode
        F[i] = F[i-1] + F[i-2] - 1
    else:
        # account for deaths
        F[i] = F[i-1] + F[i-2] - F[i-(m+1)]


# output
print(F[-1])
print(F)