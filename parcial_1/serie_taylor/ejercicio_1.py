import sys
sys.path.append('ANALISIS-NUMERICO')
import sympy as sp

from serie_taylor import serie_taylor

x = sp.symbols('x')
funcion = 2**x
P1 = serie_taylor(funcion, 1, 0)
print(P1)

