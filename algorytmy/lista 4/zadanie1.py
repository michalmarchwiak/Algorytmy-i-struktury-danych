import time
import matplotlib.pyplot as plt


class Node:
    """Klasa reprezentująca pojedynczy element listy jednokierunkowej."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Klasa reprezentująca listę jednokierunkową."""
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove_last(self):
        if not self.head:
            return None
        if not self.head.next:
            data = self.head.data
            self.head = None
            return data
        current = self.head
        while current.next.next:
            current = current.next
        data = current.next.data
        current.next = None
        return data

    def get_last(self):
        if not self.head:
            return None
        current = self.head
        while current.next:
            current = current.next
        return current.data


class Stack:
    """Klasa reprezentująca stos zbudowany na liście jednokierunkowej."""
    def __init__(self):
        self.list = LinkedList()

    def push(self, data):
        self.list.append(data)

    def pop(self):
        return self.list.remove_last()

    def top(self):
        return self.list.get_last()


# Funkcja do mierzenia czasu operacji
def measure_time(stack, operation, num_elements):
    start_time = time.time()
    if operation == "push":
        for i in range(num_elements):
            stack.push(i)
    elif operation == "pop":
        for i in range(num_elements):
            stack.pop()
    elif operation == "top":
        for i in range(num_elements):
            stack.top()
    return time.time() - start_time


# Generowanie danych dla wykresu
sizes = [10, 100, 500, 1000, 5000, 10000, 50000]
push_times = []
pop_times = []
top_times = []

for size in sizes:
    stack = Stack()
    push_times.append(measure_time(stack, "push", size))
    pop_times.append(measure_time(stack, "pop", size))
    stack = Stack()
    for i in range(size):  # Wypełniamy stos, aby móc testować top
        stack.push(i)
    top_times.append(measure_time(stack, "top", size))

# Wykres
plt.figure(figsize=(10, 6))
plt.plot(sizes, push_times, label="Push", marker='o')
plt.plot(sizes, pop_times, label="Pop", marker='o')
plt.plot(sizes, top_times, label="Top", marker='o')
plt.title("Czas wykonywania operacji na stosie zaimplementowanym na liście jednokierunkowej")
plt.xlabel("Liczba elementów")
plt.ylabel("Czas (sekundy)")
plt.legend()
plt.grid(True)
plt.show()