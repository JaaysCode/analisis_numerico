import numpy as np

def jacobi(A, b, x0, Nmax, tol):

    """
        -A: Matriz cuadrada NxN
        -b: vector
        -x0: vector inicial-- si no me da este dato se asume que el vector es el vector nulo
        -Nmax: numero maximo de iteraciones de la sucesion
        -tole: exactitud con la cual encontraremos la solucion del sistem de ecuaciones lineales
                (si no me proporciona este dato se asume que como 1e-6)
        *NOTA: TANTO LA MATRIZ COMO EL VECTOR b Y x0 DEBEN SER DE TIPO FLOAT """


    n = len(b)
    x_sol = np.zeros(n)
    error = 10
    count = 0
    while (error > tol or  count < Nmax):
        for i in range(n):
            suma = 0
            for j in range(n):
                if i != j:
                    suma += np.dot(A[i][j], x_sol[j]) 
            x_sol[i] = (b[i] - suma) / A[i,i]

        count += 1
        error = max(abs(x_sol - x0))
        x0 = np.copy(x_sol)
        print(f"Iteracion {count}: {x_sol} con error {error}")
    return x_sol


A = np.array([[3, -1, 0], [-1 ,4 ,-1], [ 0, -1, 5]], dtype=float)
b = np.array([2, 3, 5], dtype=float)
x0 = np.zeros(len(b))

print(jacobi(A, b, x0, 50, 1e-2))


