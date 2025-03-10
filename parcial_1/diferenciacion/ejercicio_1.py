"""
Paracaidista
"""
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

masa = 68.1
c = 15
gravedad = 9.8
v = [0]
v_analitica = []
h = 0.1
t_inicial = 0
t_final = 120

while t_inicial <= t_final:
    t_inicial += h
    v.append((gravedad - (c/masa)*v[-1])*h + v[-1])
    v_analitica.append((gravedad*masa/c)*(1-np.exp(-(c/masa)*t_inicial)))

error_absoluto = np.abs(v[-1] - v_analitica[-1])
print("Error absoluto: ", error_absoluto)
print("----------------------")
print(v)
plt.plot(v)
plt.show()

x = sp.symbols('x')
funcion = 10*sp.exp((-x/10)*sp.sin(2*x))
derivada = sp.diff(funcion, x)
derivada.evalf(subs={x: 1.2})
print(derivada)