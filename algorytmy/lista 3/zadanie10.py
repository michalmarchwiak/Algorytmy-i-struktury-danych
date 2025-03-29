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
            raise Empty("Stack is empty")
        return self._data.pop()

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]


class QueueUsingStacks:
    def __init__(self):
        self._stack1 = Stack()  # Stos używany do dodawania elementów
        self._stack2 = Stack()  # Stos używany do usuwania elementów

    def __len__(self):
        return len(self._stack1) + len(self._stack2)

    def is_empty(self):
        return self._stack1.is_empty() and self._stack2.is_empty()

    def enqueue(self, e):
        self._stack1.push(e)

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        if self._stack2.is_empty():  # Jeśli stack2 jest pusty, przenosimy elementy ze stack1
            while not self._stack1.is_empty():
                self._stack2.push(self._stack1.pop())
        return self._stack2.pop()

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        if self._stack2.is_empty():  # Jeśli stack2 jest pusty, przenosimy elementy ze stack1
            while not self._stack1.is_empty():
                self._stack2.push(self._stack1.pop())
        return self._stack2.top()