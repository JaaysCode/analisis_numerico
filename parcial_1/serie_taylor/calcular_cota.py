import sympy as sp
import numpy as np
from math import factorial

def calcular_cota(funcion, grado, x0, x_point):
    derivada = sp.diff(funcion, x, grado + 1)
    derivada = sp.lambdify(x, derivada)

    #preguntar que es u_x
    u_x = np.linspace(min(x0, x_point), max(x_point, x0), 1000)

    maximo = max(np.abs(derivada(u_x)))
    R_x = maximo * (x_point - x0) ** (grado + 1) / factorial(grado + 1)
    return np.abs(R_x)

x = sp.symbols('x')
funcion_prueba = 2**x
cota_prueba = calcular_cota(funcion_prueba, 4, 2, 1.5)
print(f"cota maxima {cota_prueba}")