import timeit
import matplotlib.pyplot as plt

# Lista różnych rozmiarów wejściowych do testów
input_sizes = [100, 1000, 10000, 100000, 1000000, 10000000, 20000000]

# Funkcja do przeprowadzania testów czasu dla danej metody i rozmiaru wejścia
def run_time_tests(input_size, method):
    test_list = list(range(input_size))
    if method == 'append':
        def test():
            result = []
            for item in test_list:
                result.append(item)
    elif method == 'extend':
        def test():
            result = []
            result.extend(test_list)
    return [timeit.timeit(test, number=1) for _ in range(10)]  # wykonanie 10 prób dla danego rozmiaru wejścia

# Przeprowadzanie eksperymentów dla obu metod przy różnych rozmiarach wejścia
append_times = [run_time_tests(size, 'append') for size in input_sizes]
extend_times = [run_time_tests(size, 'extend') for size in input_sizes]

# Obliczanie średnich czasów dla wykresu
avg_append_times = [sum(times) / len(times) for times in append_times]
avg_extend_times = [sum(times) / len(times) for times in extend_times]

# Tworzenie wykresu porównawczego
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, avg_append_times, label='Metoda append', marker='o')
plt.plot(input_sizes, avg_extend_times, label='Metoda extend', marker='s')
plt.title('Porównanie czasu wykonania metod append i extend dla różnych rozmiarów wejścia')
plt.xlabel('Rozmiar wejścia')
plt.ylabel('Średni czas wykonania (sekundy)')
plt.legend()
plt.grid(True)
plt.show()