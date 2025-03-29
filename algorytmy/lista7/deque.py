class Empty(Exception):
    pass

class Deque:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * Deque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._data[self._front]

    def last(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        back = (self._front + self._size - 1) % len(self._data)
        return self._data[back]

    def enqueue_front(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1

    def enqueue_back(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def dequeue_front(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        value = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1

        if 0 < self._size < len(self._data) // 4 and len(self._data) > Deque.DEFAULT_CAPACITY:
            self._resize(len(self._data) // 2)
        return value

    def dequeue_back(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        back = (self._front + self._size - 1) % len(self._data)
        value = self._data[back]
        self._data[back] = None
        self._size -= 1
        if 0 < self._size < len(self._data) // 4 and len(self._data) > Deque.DEFAULT_CAPACITY:
            self._resize(len(self._data) // 2)
        return value

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0