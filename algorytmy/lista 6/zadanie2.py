import time
import matplotlib.pyplot as plt
import random


class BinaryHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_down(self, index):
        size = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == index:
                break
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]


def heap_sort(arr):
    heap = BinaryHeap()
    for element in arr:
        heap.insert(element)
    sorted_list = []
    while len(heap.heap) > 0:
        sorted_list.append(heap.remove())
    return sorted_list


def measure_performance():
    list_sizes = [100, 500, 1000, 5000, 10000, 20000, 50000]
    times = []

    for size in list_sizes:
        test_list = [random.randint(1, 1000000) for _ in range(size)]
        start_time = time.time()
        heap_sort(test_list)
        end_time = time.time()
        times.append(end_time - start_time)

    return list_sizes, times


def plot_results(list_sizes, times):
    plt.figure(figsize=(10, 6))
    plt.plot(list_sizes, times, marker='o')
    plt.title("Czas działania heap_sort dla różnych rozmiarów listy")
    plt.xlabel("Rozmiar listy")
    plt.ylabel("Czas działania (s)")
    plt.grid()
    plt.show()


list_sizes, times = measure_performance()
plot_results(list_sizes, times)