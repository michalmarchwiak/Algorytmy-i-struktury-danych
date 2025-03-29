def quicksort_iterative(arr):
    """Sortowanie szybkie bez rekurencji, działające in-place"""
    stack = [(0, len(arr) - 1)]  # Stos przechowujący zakresy do posortowania

    while stack:
        low, high = stack.pop()  # Pobieramy zakres ze stosu
        if low < high:
            # Podział tablicy i uzyskanie indeksu pivota
            pivot_index = partition(arr, low, high)

            # Dodajemy zakresy podtablic do stosu
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))


def partition(arr, low, high):
    """Funkcja dzieląca tablicę wokół pivota"""
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Zamieniamy pivot na właściwą pozycję
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # Zwracamy indeks pivota


tab = [12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5, 0, 0, 2, 4]
quicksort_iterative(tab)
print("Posortowana tablica:", tab)