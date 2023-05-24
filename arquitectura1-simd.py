"""
Se necesita instalar la libreria "numpy" para poder ejecutar este programa.
Para poder instalar la libreria numpy tenemos que ejecutar el siguiente comando: pip install numpy
"""
# Ejercicio 2: Diseñe un programa que multiplique dos matrices de 2 dimensiones
import numpy as np
import time

def matriz_simd(matriz_a, matriz_b):
    start = time.time()
    # numpy internamente utiliza SIMD para realizar la multiplicación de matrices
    resultado = np.multiply(matriz_a, matriz_b)
    end = time.time()
    return resultado, (end - start)

if __name__ == '__main__':
    # Matrices de entrada
    matriz_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matriz_b = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

    # Realizar la multiplicación de matrices utilizando SIMD(Single Instruction Multiple Data)
    resultado_simd, tiempo_ejecucion = matriz_simd(matriz_a, matriz_b)

    print("Resultado SIMD:")
    print(resultado_simd)
    print("Tiempo de ejecución:", tiempo_ejecucion, "segundos")
