"""
La cantidad de un contaminante radiactivo distribuido uniformemente que se
encuentra contenido en un reactor cerrado, se mide por su concentración c
(becquerel/litro, o Bq/L). El contaminante disminuye con una tasa de decaimiento
proporcional a su concentración, es decir: dc/dt = -kc

Determine la cantidad de contaminante radioactivo desde un tiempo [0,1] día. La
concentración inicial es de 10Bq/L, tome un h = 0.1 y k = 0.25

Grafique la solución
"""
import matplotlib.pyplot as plt

concentraciones = [10]
h = 0.1
k = 0.25
concentracion_inicial = 10
tiempo = 0
tiempo_total = 1
tiempos = [0]
while tiempo <= tiempo_total:
    concentraciones.append(-k*h*concentracion_inicial + concentracion_inicial)
    tiempos.append(tiempo)
    tiempo += h

print(concentraciones)
plt.plot(tiempos, concentraciones, marker = 'o')
plt.xlabel('Tiempo (dias)')
plt.ylabel('Concentra9cion (Bq/L)')
plt.title('Decaimiento del contaminante radioactivo')
plt.grid(True)
plt.show()

