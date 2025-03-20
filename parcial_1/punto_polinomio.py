"""
Sea f(x)=(1+x)2ln(1+x)

1. Determine el segundo polinomio de Taylor P2(x) para la función f(x) en torno a x0=0.
2. Use P2(0.5) para aproximar f(0.5). Determine una cota superior para el error |f(0.5)−P2(0.5)| por medio
de la fórmula de error y compárela con el error real.
3. Aproxime ∫0.5−0.5f(x)dx usando ∫0.5−0.5P2(x)dx.
"""

import sympy as sp
from math import factorial
import numpy as np

x = sp.symbols('x')

def serie_taylor(funcion, grado, x0):
    polinomio = 0
    for i in range(grado + 1):
        derivada = sp.diff(funcion, x, i)
        derivada_evaluada = derivada.evalf(subs={x: x0})
        polinomio += derivada_evaluada * (x - x0) ** i / factorial(i)
    return polinomio


def calcular_cota(funcion, grado, x0, x_point):
    derivada = sp.diff(funcion, x, grado + 1)
    derivada = sp.lambdify(x, derivada)

    u_x = np.linspace(min(x0, x_point), max(x_point, x0), 1000)

    maximo = max(np.abs(derivada(u_x)))
    R_x = maximo * (x_point - x0) ** (grado + 1) / factorial(grado + 1)
    return np.abs(R_x)




#Funcion dada

funcion = ((1 + x)**2)*sp.ln(1 + x)

# PRIMER PUNTO
P2 = serie_taylor(funcion, 2, 0)
print(f"P2(x) = {P2}")

#SEGUNDO PUNTO
P2_05 = P2.evalf(subs={x: 0.5})
f_05 = funcion.evalf(subs={x: 0.5})
error = abs(f_05 - P2_05)
cota_error_p2 = calcular_cota(funcion, 2, 0, 0.5)

print(f"Error real: {error}")
print(f"Cota de error: {cota_error_p2}")

#TERCER PUNTO
integral_f = sp.integrate(funcion,(x, -0.5, 0.5))
integral_p2 = sp.integrate(P2,(x, -0.5, 0.5))

print(f"integral de f(x) = {integral_f} \n integral de P2(x) = {integral_p2}")