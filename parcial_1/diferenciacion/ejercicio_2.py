import sympy as sp

x = sp.symbols('x')
funcion = 10*sp.exp((-x/10))*sp.sin(2*x)
derivada = sp.diff(funcion, x)
print(derivada)
print(derivada.evalf(subs={x: 1.2}))
