import os


def find(path, filename):
    found_files = []

    # Przechodzimy przez wszystkie elementy w danej ścieżce
    for item in os.listdir(path):
        full_path = os.path.join(path, item)

        # Sprawdzamy, czy element jest katalogiem
        if os.path.isdir(full_path):
            # Rekurencyjne wywołanie dla podkatalogu
            found_files.extend(find(full_path, filename))
        elif item == filename:
            # Dodajemy do listy, jeśli nazwa pliku się zgadza
            found_files.append(full_path)

    return found_files

# Przykład użycia:
# wyniki = find('/ścieżka/do/folderu', 'szukany_plik.txt')
# print(wyniki)
