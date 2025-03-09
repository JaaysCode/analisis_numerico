import sympy as sp

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

x = sp.symbols('x')
funcion_prueba = x**2 - 6
print(newton(funcion_prueba, 1e-4, 1))