"""
La policía descubre el cuerpo de un inversionista. Para resolver el crimen es decisivo
determinar cuando se cometió el homicidio. El forense llegó al medio día y de
inmediato observa que la temperatura del cuerpo es de 30◦C . Así mismo, observa que
la temperatura de la habitación es constante a 27◦C . Suponiendo que la temperatura
de la víctima era normal en el momento de su fallecimiento (37◦C ), determinar la
hora en que se cometió el crimen. La ecuación diferencial es:
dT
dt = k(T − Ta)
con k = -0.4056
"""

import matplotlib.pyplot as plt

k = -0.4056
temperatura = [37]
temperatura_ambiente = 27
h = 0.01
tiempo_muerte = 0
tiempo_encuentro = 12

while temperatura[-1] > 30:
    temperatura.append((-h*(k*(temperatura[-1] - temperatura_ambiente)) + temperatura[-1]))
    tiempo_muerte += h

print(tiempo_muerte)