class MaxBinaryHeap:
    def __init__(self, n):
        self.heap = []
        self.n = n

    def __str__(self):
        return str(self.heap)

    def insert(self, key):
        """
        Wstawia nowy element do kopca.
        """
        if len(self.heap) < self.n:
            self.heap.append(key)
            self._heapify_up(len(self.heap) - 1)
        else:
            # Jeśli kopiec jest pełny, zastępujemy najmniejszy element, jeśli nowy klucz jest większy
            if key > self.heap[-1]:
                self.heap[-1] = key
                self._heapify_up(len(self.heap) - 1)
        self._move_min_to_end()

    def _heapify_up(self, index):
        """
        Naprawia kopiec przez przesuwanie elementu 'do góry'.
        """
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index):
        """
        Naprawia kopiec przez przesuwanie elementu 'w dół'.
        """
        size = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            if left < size and self.heap[left] > self.heap[largest]:
                largest = left
            if right < size and self.heap[right] > self.heap[largest]:
                largest = right
            if largest == index:
                break
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest

    def _move_min_to_end(self):
        """
        Przesuwa najmniejszy element na koniec listy.
        """
        if not self.heap:
            return

        min_index = 0
        for i in range(1, len(self.heap)):
            if self.heap[i] < self.heap[min_index]:
                min_index = i

        self.heap[min_index], self.heap[-1] = self.heap[-1], self.heap[min_index]


hip = MaxBinaryHeap(8)
hip.insert(1)
print(hip)
hip.insert(1)
print(hip)
hip.insert(10)
print(hip)
hip.insert(5)
print(hip)
hip.insert(7)
print(hip)
hip.insert(2)
print(hip)
hip.insert(3)
print(hip)
hip.insert(4)
print(hip)
hip.insert(5)
print(hip)
hip.insert(6)
print(hip)
hip.insert(7)
print(hip)
hip.insert(8)
print(hip)
