import numpy as np

#Declarar la matriz A y el vector de terminos independientes b

A = np.array([[0, 2, 1], [6, -8, -2], [1, -1, -2]])
b = np.array([2, 1, 3])

#Entradas tipo flotante
def eliminacion_gaussiana(A, b):
    
    A = A.astype(float)
    b = b.astype(float)
    n = len(b)

    for filas in range(n - 1):

        if abs(A[filas][filas]) < 1e-10:

            max_fila = np.argmax(abs(A[filas:, filas])) + filas
            A[[filas, max_fila]] = A[[max_fila, filas]]
            b[[filas, max_fila]] = b[[max_fila, filas]]

        for columnas in range(filas + 1, n):
            factor = A[columnas][filas] / A[filas][filas]
            A[columnas] = A[columnas] - factor * A[filas]
            b[columnas] = b[columnas] - factor * b[filas]
            print(factor)

    #Regresion hacia atras
    x = np.zeros(n)
    for k in range (n - 1, -1, -1):
        x[k] = (b[k] - np.dot(A[k,k+1:n], x[k+1:n])) / A[k,k]

    return x
        
print(eliminacion_gaussiana(A, b))
