import numpy as np

def metodo_euler(ecuacion_diferencial, a, b, h, condicion_inicial):
    """
    Implementación del método de Euler para resolver ecuaciones diferenciales de primer orden.

    Parámetros:
        ecuacion_diferencial : función f(t, y) que representa la ecuación diferencial
        a : límite inferior del intervalo
        b : límite superior del intervalo
        h : Espaciamiento para generar los valores de t 
        condicion_inicial: valor inicial y(t0)
        
    Retorna:
        tiempos (list): lista de tiempos t
        valores (list): lista de soluciones y(t)
    """
    # Calcular número de pasos (convertido a entero)
    n = int((b - a) / h)
    
    # Inicializar listas de tiempos y valores
    tiempos = [a]
    valores = [condicion_inicial]
    
    # Para sistemas de ecuaciones diferenciales (como en presa-depredador)
    es_sistema = isinstance(condicion_inicial, (list, np.ndarray)) and len(np.array(condicion_inicial).shape) > 0
    
    # Iterar para calcular los valores en cada paso
    for i in range(n):
        t_actual = a + i * h
        y_actual = valores[i]
        
        # Calcular el siguiente valor usando la fórmula de Euler
        if es_sistema:
            # Para sistemas de EDOs
            y_siguiente = y_actual + h * ecuacion_diferencial(t_actual, y_actual)
        else:
            # Para EDOs escalares
            y_siguiente = y_actual + h * ecuacion_diferencial(t_actual, y_actual)
        
        # Añadir el nuevo tiempo y valor a las listas
        tiempos.append(t_actual + h)
        valores.append(y_siguiente)
    
    return tiempos, valores
