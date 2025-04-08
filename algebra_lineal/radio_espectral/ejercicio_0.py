import numpy as np

A = np.array([[-1, 2, 0],
          [2, -3, 1],
          [0, 1, 2]])

l,v = np.linalg.eig(A)
radio_espectral = max(abs(l))
print(l)
print("\n")
print(radio_espectral)
