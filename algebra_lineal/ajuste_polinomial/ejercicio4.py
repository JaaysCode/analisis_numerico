import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from metodo_gauus_seidel import gauss_seidel

Px = np.array([0, 6, 10, 13, 17, 20, 28])
hojas_jovenes = np.array([6.67, 17.33, 42.67, 37.33, 30.10, 29.31, 28.74])
hojas_maduras = np.array([6.67, 16.11, 18.89, 15.00, 10.56, 9.44, 8.89])


def Matrix(Px):
    n = len(Px)
    B = np.zeros([n,n])
    for i in range(n):
        for j in range(n):
            B[i,j] = Px[i]**j  # Corregido: cada elemento es x_i elevado a la j
    
    return B

tol =  1e-6
x0_hojas_jovenes = np.zeros_like(hojas_jovenes)
x0_hojas_maduras = np.zeros_like(hojas_maduras)

coeficientes_hojas_jovenes= gauss_seidel(Matrix(Px), hojas_jovenes, x0_hojas_jovenes, tol)
coeficientes_hojas_maduras = gauss_seidel(Matrix(Px), hojas_maduras, x0_hojas_maduras, tol)
print(f'Coeficientes hojas jovenes: {coeficientes_hojas_jovenes}')
print(f'Coeficientes hojas maduras: {coeficientes_hojas_maduras}')

polinomio_hojas_jovenes = lambda x: (sum(coeficientes_hojas_jovenes[i]*x**i for i in range(len(coeficientes_hojas_jovenes))))
polinomio_hojas_maduras = lambda x: (sum(coeficientes_hojas_maduras[i]*x**i for i in range(len(coeficientes_hojas_maduras))))
u_x = np.linspace(min(Px), max(Px), 100)

# Crear dos subplots (gráficas separadas)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

# Gráfica para hojas jóvenes
ax1.plot(Px, hojas_jovenes, 'o', label="Datos observados")
ax1.plot(u_x, polinomio_hojas_jovenes(u_x), label="Polinomio interpolador")
ax1.set_title("Hojas Jóvenes")
ax1.set_xlabel("Días")
ax1.set_ylabel("Número de hojas")
ax1.legend()
ax1.grid(True)

# Gráfica para hojas maduras
ax2.plot(Px, hojas_maduras, 'o', label="Datos observados")
ax2.plot(u_x, polinomio_hojas_maduras(u_x), label="Polinomio interpolador")
ax2.set_title("Hojas Maduras")
ax2.set_xlabel("Días")
ax2.set_ylabel("Número de hojas")
ax2.legend()
ax2.grid(True)

plt.tight_layout()  # Ajusta el espacio entre las gráficas
plt.show()

x = sp.symbols('x')

valor_promedio_hojas_jovenes = (1/28) * sp.integrate(polinomio_hojas_jovenes(x), (x, 0, 28))
valor_promedio_hojas_maduras = (1/28) * sp.integrate(polinomio_hojas_maduras(x), (x, 0, 28))
print(f'El valor promedio de hojas jóvenes es: {valor_promedio_hojas_jovenes}')
print(f'El valor promedio de hojas maduras es: {valor_promedio_hojas_maduras}')
#valor_promedio = (1/28) * (sp.integrate())