"""
Suponga que un alumno es portador del virus de la gripe y regresa a su escuela donde
hay 1000 estudiantes. Si se supone que la constante de proporción del modelo es
k = 0.0009906 con que se propaga al virus no sólo a la cantidad x de alumnos
infectados, sino también a la cantidad de alumnos no infectados, determinar la
cantidad de alumnos infectados seis días después
El modelo es : dx/dt = kx (1000 − x )
Calcular la cantidad de contagiado al cabo de 6 días
Realizar una gráfica de la información de: los contagiados y los no contagiados.
"""

import matplotlib.pyplot as plt

infectados = [1]
no_infectados = [999]

k = 0.0009906
h = 0.01
t_inicial = 0
t_final = t_inicial + h

while t_inicial <= 6:
    nuevos_infectados = (h*(k*infectados[-1])*(1000 - infectados[-1])) + infectados[-1]
    infectados.append(nuevos_infectados)
    no_infectados.append(1000 - nuevos_infectados)
    t_inicial += h

print(infectados[-1])

plt.plot(infectados, label="Infectados")
plt.plot(no_infectados, label="No infectados")
plt.show()



