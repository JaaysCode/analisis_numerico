import numpy as np
import matplotlib.pyplot as plt
from metodo_jacobi_matrices import jacobi_con_matrices 

Px = np.array([1,2,5])

n = len(Px)
B = np.zeros([n,n])
for i in range(n):
    B[i,0] = 1


print(B)