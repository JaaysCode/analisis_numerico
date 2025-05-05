import numpy as np
import matplotlib.pyplot as plt
from metodo_gauus_seidel import gauss_seidel
Px = np.array([1,2,5,10,20,30,40])
Ty = np.array([56.5, 78.6, 113, 144.5, 181.0, 205, 214.5])

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
coeficientes = gauss_seidel(Matrix(Px), Ty, x0, tol)
print(coeficientes)

u_x = np.linspace(min(Px), max(Px), 100)
#Pol2 = lambda x: coeficientes[0] + coeficientes[1]*x + coeficientes[2]*x**2 + coeficientes[3]*x**3 + coeficientes[4]*x**4 + coeficientes[5]*x**5 + coeficientes[6]*x**6
Pol2 = lambda x: sum(coeficientes[i]*x**i for i in range(len(coeficientes)))
plt.plot(Px, Ty, 'o', label= "Datos observados")
plt.plot(u_x, Pol2(u_x), label ="polinomio grado 6")
plt.legend()
plt.show()  # Esta línea muestra la gráficas
print(f'La aproximacion para una presio de P = 35 atm es: {Pol2(35)}' )