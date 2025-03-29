3

import time
import random
import matplotlib.pyplot as plt
import numpy as np

# Funkcja do pomiaru czasu sortowania
def measure_sorting_time(n):
    data = [random.randint(1, 10000) for _ in range(n)]
    start_time = time.time()
    sorted_data = sorted(data)
    end_time = time.time()
    return end_time - start_time

# Funkcja złożoności czasowej O(n log n)
def nlogn(n):
    return n * np.log(n)

# Rozmiary danych wejściowych
input_sizes = [10, 100, 1000, 10000, 100000]

# Pomiar czasu sortowania dla różnych rozmiarów danych
execution_times = [measure_sorting_time(n) for n in input_sizes]

# Generuje wykres
plt.plot(input_sizes, execution_times, marker='o', label='Czas sortowania')
plt.plot(input_sizes, [nlogn(n) for n in input_sizes], label='O(n log n)', linestyle='--', color='red')
plt.xscale('log')  # Skala logarytmiczna na osi x
plt.yscale('log')  # Skala logarytmiczna na osi y
plt.xlabel('Rozmiar danych wejściowych (n)')
plt.ylabel('Czas sortowania (s)')
plt.title('Czas sortowania za pomocą sorted() w zależności od rozmiaru danych')
plt.legend()
plt.grid(True)
plt.show()
