class Empty(Exception):
    pass

class Stack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

def generate_permutations(n):
    stack = Stack()
    stack.push(([], set(range(1, n + 1))))  # Pusta permutacja i zbiór liczb {1, ..., n}

    while not stack.is_empty():
        current_perm, remaining = stack.pop()  # Pobieramy częściową permutację i zbiór

        if not remaining:  # Jeśli brak pozostałych liczb, mamy pełną permutację
            print(current_perm)
        else:
            for num in remaining:  # Dla każdej liczby w zbiorze pozostałych
                # Tworzymy nową permutację i nowy zbiór liczb
                new_perm = current_perm + [num]
                new_remaining = remaining - {num}
                stack.push((new_perm, new_remaining))  # Dodajemy na stos

import time
start = time.time()
generate_permutations(3)
end = time.time()
print(end-start)