class Empty(Exception):
    pass

class Queue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self.data = [None] * Queue.DEFAULT_CAPACITY
        self._size = 0
        self.front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self.data[self.front]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        value = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self._size -= 1

        if 0 < self._size < len(self.data) // 3 and len(self.data) > Queue.DEFAULT_CAPACITY:
            self._resize(len(self.data) // 2)

        return value

    def enqueue(self, e):
        if self._size == len(self.data):
            self._resize(2 * len(self.data))
        avail = int((self.front + self._size) % len(self.data))
        self.data[avail] = e
        self._size += 1

    def _resize(self, cap):
        old = self.data
        self.data = [None] * cap
        walk = self.front
        for k in range(self._size):
            self.data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self.front = 0