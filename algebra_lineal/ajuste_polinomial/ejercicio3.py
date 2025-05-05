import numpy as np
import matplotlib.pyplot as plt
from eliminacion_pivoteo import eliminacion_gaussiana

Px = np.array([1960, 1970, 1980, 1990, 2000, 2010])
Ty = np.array([179323, 203302, 226542, 249633, 281422, 308746])

def Matrix(Px):
    n = len(Px)
    B = np.zeros([n,n])
    for i in range(n):
        B[i,0] = 1
        for j in range(1, n):
            B[i,j] = B[i,j-1]*Px[i]
    
    return B

tol =  1e-6
x0 = np.zeros_like(Ty)
coeficientes = eliminacion_gaussiana(Matrix(Px), Ty)
print(coeficientes)
u_x = np.linspace(min(Px) - 10, max(Px) + 10, 100)
Pol2 = lambda x: sum(coeficientes[i]*x**i for i in range(len(coeficientes)))
plt.plot(Px, Ty, 'o', label= "Datos observados")
plt.plot(u_x, Pol2(u_x), label ="polinomio grado 5")

plt.plot(1950, Pol2(1950), 'ok')
plt.plot(1975, Pol2(1975), 'ok')
plt.plot(2014, Pol2(2014), 'ok')
plt.plot(2020, Pol2(2020), 'ok')

plt.legend()
plt.show()
print(f'La aproximacion para la poblacion en 1950 es: {Pol2(1950)}' )
print(f'La aproximacion para la poblacion en 1975 es: {Pol2(1975)}' )
print(f'La aproximacion para la poblacion en 2014 es: {Pol2(2014)}' )
print(f'La aproximacion para la poblacion en 2020 es: {Pol2(2020)}' )