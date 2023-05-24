"""
Ejercicio 2: Diseñe un programa que cuente el número de vocales en un texto
"""

import multiprocessing
import time

def count_vowels(text):
  vowels = ['a', 'e', 'i', 'o', 'u']
  count = 0
  for letter in text:
    if letter in vowels:
      count += 1
  return count

if __name__ == "__main__":
  # Textos de entrada
  texts = ["Rust", "JavaScript", "Java"]

  # Crea un pool de procesos
  pool = multiprocessing.Pool()

  # Inicia el cronometro
  start = time.time()

  # Realiza el conteo de vocales en cada texto
  results = pool.map(count_vowels, texts)

  # Detiene el cronometro
  end = time.time()

  # Imprime los resultados
  print("Resultados parciales:", results)
  print("Tiempo de ejecución:", tiempo_ejecucion, "segundos")
