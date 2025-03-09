import sympy as sp
from math import factorial

x = sp.symbols('x')

def serie_taylor(funcion, grado, x0):
    polinomio = 0
    for i in range(grado + 1):
        derivada = sp.diff(funcion, x, i)
        derivada_evaluada = derivada.evalf(subs={x: x0})
        polinomio += derivada_evaluada * (x - x0) ** i / factorial(i)
    return polinomio
