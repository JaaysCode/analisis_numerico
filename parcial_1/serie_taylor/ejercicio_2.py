"""
Determinar los polinomios de grado 1, 2, 4, 6 de la funcion Ln(x^2 + 1), entorno a X_0 = 1,
Hacer las graficas en un mismo plot
Aproximar ciertos datos usando el polinomio  (pandas)
"""
import sympy as sp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from serie_taylor import serie_taylor as st
x = sp.Symbol('x')
funcion = sp.log(x**2 + 1)
tabla = []

polinomios = {
    0: st(funcion, 1, 1),
    1: st(funcion, 2, 1),
    2: st(funcion, 4, 1),
    3: st(funcion, 6, 1)
}

for i in range(len(polinomios)):
    for k in [0, 0.5, 4]:
        polinomio_aproximado = polinomios[i].evalf(subs={x:k})
        funcion_real = funcion.evalf(subs={x:k})
        error_absoluto = np.abs(polinomio_aproximado - funcion_real)
        error_relativo = np.abs(error_absoluto/funcion_real)
        tabla.append([k, polinomio_aproximado, funcion_real, error_absoluto, error_relativo])

df = pd.DataFrame(tabla, columns=['X', 'P(x)', 'f(x)', 'Error Absoluto = |P(x) - f(x)|', 'Error relativo'])

for i, group in df.groupby(df.index // 3):
    print(f"P{i+1}:\n{group}\n")

plt.figure(figsize=(10, 6))
x_vals = np.linspace(-2, 5, 400)

for i in range(4):
    y_vals = [polinomios[i].evalf(subs={x:val}) for val in x_vals]
    plt.plot(x_vals, y_vals, label=f'Polinomio {i+1}')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Aproximacion de Polinomios de Taylor')
plt.legend()
plt.grid(True)
plt.show()