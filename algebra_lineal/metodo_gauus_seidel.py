"""
Este código implementa el método de Gauss Seidel utilizando matrices para resolver sistemas de ecuaciones lineales.
"""
import numpy as np

import time

def gauss_seidel(A, b, x0, tol):
    """
    Implementación del método de Gauss Seidel.
    -----------
    Parámetros
    -----------
    - A: matriz de coeficientes cuadrada
    - b: vector de términos independientes
    - x0: vector inicial --> Si no me da el dato se asume que el vector es el vector nulo
    - tol: Exactitud con la cual encontraremos la solución del sistema de ecuaciones lineales (SEL). Si no me dan este dato se asume que la tolerancia es 1e-6
    -----------
    Nota
    ------------
    - TANTO LA MATRIZ A COMO EL VECTOR b Y X0 TIENEN QUE SER DE TIPO FLOTANTE
    - AMBAS TIENE QUE TENER DIAGONAL ESTRICTAMENTE DOMINANTE
    """
    D = np.diag(np.diag(A)) # Obtenemos la matriz diagonal
    L = D - np.tril(A) # Obtenemos la matriz inferior
    U = D - np.triu(A) # Obtenemos la matriz superior
    Tg = np.dot(np.linalg.inv(D-L), U)
    Cg = np.dot(np.linalg.inv(D-L), b)
    v_propios, vect_propios = np.linalg.eig(Tg)
    radio = max(abs(v_propios))
    #print(f"Radio espectral: {radio}")
    if radio<1:
        time_start = time.time()
        error = 1
        iteracion = 1
        while (error > tol):
            x1 = np.dot(Tg,x0) + Cg
            error = np.max(np.abs(x1-x0))
            x0 = np.copy(x1)
            # print(f"Iteración {iteracion}: {x1}, Error: {error}")
            iteracion += 1
        time_end = time.time()
        time_total = time_end - time_start
        return x0
            
    else:
        print("El sistema iterativo no converge con el método de Jacobi")


A = np.array([[3, -1, 0], [-1, 4, -1], [0, -1, 5]], dtype=float)
b = np.array([2, 3, 5], dtype=float)
tol = 1e-6
x0 = np.zeros_like(b)

solucion = gauss_seidel(A, b, x0, tol)
print("La solución es:", solucion)
#print("El error es:", error)
#print("El tiempo de cómputo es:", tiempo)