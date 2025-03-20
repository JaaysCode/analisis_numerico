"""
Un objeto con masa de 80kg, inicialmente en reposo, se deja caer al agua desde un barco y se sumerge.
Mientras la gravedad atrae al objeto hacia abajo, una fuerza de boyanza $b_z$ igual a $\frac{1}{20}$ del peso del
objeto lo empuja hacia arriba. Se supone que la resistencia del agua ejerce una fuerza sobre el objeto que es
proporcional a la velocidad del propio objeto, con constante de proporcionalidad igual a 15kg/s,.
La ecuación diferencial que describe la situación es: 

"""
import matplotlib.pyplot as plt


masa = 80
gravedad = -9.8
b = (1/20)*masa
k = 15
velocidades = [0]
h = 0.01
t_inicial = 0
t_final = t_inicial + h

while velocidades[-1] < 70:
    velocidades.append(h*(gravedad-(b*gravedad)-((k*velocidades[-1])/masa)) + velocidades[-1])
    t_final += h
    if velocidades[-1] == 70:
        break

print(f"Los segundos que transcurrieron hasta que la velocidad del objeto fue 70 m/s fueron: {t_final}")
plt.plot(velocidades)
plt.xlabel('Tiempo (milisegundo)')
plt.ylabel('Velocidad (m/s)')
plt.show()
