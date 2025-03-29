class Empty(Exception):
    pass

class Queue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * Queue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        value = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1

        if 0 < self._size < len(self._data) // 3 and len(self._data) > Queue.DEFAULT_CAPACITY:
            self._resize(len(self._data) // 2)

        return value

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0




class StackUsingQueue:
    def __init__(self):
        self._queue = Queue()

    def __len__(self):
        return len(self._queue)

    def is_empty(self):
        return self._queue.is_empty()

    def push(self, e):
        self._queue.enqueue(e)  # Dodaj element na koniec kolejki
        # Obracanie kolejki, aby nowo dodany element był na początku
        for _ in range(len(self._queue) - 1):
            self._queue.enqueue(self._queue.dequeue())

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._queue.dequeue()  # Usuwamy pierwszy element z kolejki

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        top_element = self._queue.first()  # Odczytujemy pierwszy element
        return top_element

    # push - O(n)
    # pop - O(1)
    # top - O(1)

