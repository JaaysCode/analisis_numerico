import sympy as sp
import numpy as np

def biseccion(funcion, a, b, tolerancia):

    if funcion(a)*funcion(b)>0:
        print("La funcion no cumple el teorema en el intervalo dado")
        return
    else:
        print("Buscandoooo")
        contador = 0
        while abs(b - a) > tolerancia:
            p = (a + b) / 2
            contador += 1
            if funcion(a)*funcion(p) > 0:
                a = p
            else:
                b = p
        return contador, p


def falsa_posicion(funcion, a, b, tolerancia):

    if funcion(a)*funcion(b)>0:
        print("La funcion no cumple el teorema en el intervalo dado")
        return
    else:
        print("Buscandoooo")
        contador = 0
        p = b - funcion(b)*(a - b) / (funcion(a) - funcion(b))
        while abs(funcion(p)) > tolerancia:
            p = b - funcion(b)*(a - b) / (funcion(a) - funcion(b))
            contador += 1
            if funcion(a)*funcion(p) > 0:
                a = p
            else:
                b = p
        return contador, p

def newton(funcion, tolerancia, x):
    x_symb = sp.symbols('x')

    fdx = sp.diff(funcion, x_symb)

    fdx = sp.lambdify(x_symb, fdx)
    funcion = sp.lambdify(x_symb, funcion)

    while abs(funcion(x)) > tolerancia:
        x = x - funcion(x)/fdx(x)
    return x

def secante(funcion, tolerancia, x0, x1):

    contador = 0
    error = 1
    while error > tolerancia:
        contador +=1
        x2 = x1 - funcion(x1)*(x0 - x1) / (funcion(x0) - funcion(x1))
        error = abs(x2 - x1)
        x0 = x1
        x1 = x2
    return contador, x2

radio = 1
volumen = 0.75
funcion = lambda h: ((np.pi*h**2)*(3*radio - h))/3 - volumen
print(secante(funcion, 10e-6, 1, 2))

