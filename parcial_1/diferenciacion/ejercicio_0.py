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
h = 0.1 #horas
k = 0.25
tiempo_inicial = 0
tiempo_final =  tiempo_inicial + h#horas


while (tiempo_final <= 24):
    concentraciones.append(-k*concentraciones[-1]*h + concentraciones[-1])
    tiempo_final += h

print(concentraciones)
plt.plot(concentraciones)
plt.show()
