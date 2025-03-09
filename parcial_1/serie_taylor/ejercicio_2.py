"""
Determinar los polinomios de grado 1, 2, 4, 6 de la funcion Ln(x^2 + 1), entorno a X_0 = 1,
Hacer las graficas en un mismo plot
Aproximar ciertos datos usando el polinomio  (pandas)
"""
import sympy as sp
from serie_taylor import serie_taylor as st
x = sp.Symbol('x')
funcion = sp.log(x**2 + 1)

polinomios = {
    0: st(funcion, 1, 1),
    1: st(funcion, 2, 1),
    2: st(funcion, 6, 1),
    3: st(funcion, 6, 1)
}

polinomio_aproximado = polinomios[1].evalf(subs={x: 0})
print(polinomio_aproximado)
