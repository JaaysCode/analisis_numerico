import numpy as np
import matplotlib.pyplot as plt

from metodo_jacobi_matrices import jacobi_con_matrices 

Px = np.array([1, 2, 5, 10, 20, 30])
Ty = np.array([56.5, 78.6, 113, 144.5, 181.0, 205])

A = np.array([[1,1], [1,5]], dtype=float)
b = np.array([56.5, 113], dtype=float)

tol = 1e-6

x0 = np.zeros_like(b)
resultado = jacobi_con_matrices(A, b, x0, tol)
coeficientes = resultado[0]  # El primer elemento de la tupla es el vector solución

Pol = lambda x: coeficientes[0] + coeficientes[1]*x
u_x = np.linspace(min(Px), max(Px), 100)
plt.plot(Px, Ty, 'o', label= "Datos observados")
plt.plot(u_x, Pol(u_x), label ="polinomio grado 1")
plt.legend()
plt.show()  # Esta línea muestra la gráfica

Px = np.array([1, 2, 5, 10, 20, 30, 40])
