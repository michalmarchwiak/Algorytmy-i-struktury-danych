import ctypes #tablice niskopoziomowe

class DynamicArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)
    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError("Błędny indeks")
        return self._A[k]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        return (c * ctypes.py_object)()


    def insert(self, k, index):
        if index < 0 or index > self._n:
            print("Błędny indeks")
            return

        if self._n == self._capacity:
            self._resize(2 * self._capacity)

        for i in range(self._n - 1, index - 1, -1):
            self._A[i + 1] = self._A[i]

        self._A[index] = k
        self._n += 1

    def remove(self, index):
        if self._n == 0:
            print("Tablica jest pusta")
            return

        if index < 0 or index >= self._n:
            return IndexError("Indeks poza zasięgiem")

        if index == self._n - 1:
            self._A[index] = 0
            return

        for i in range(index, self._n - 1):
            self._A[i] = self._A[i + 1]

        self._A[self._n - 1] = 0

    def __str__(self):
        st = []
        for i in range(self._n):
            st.append(self._A[i])
        return st

    def extend(self, seq):
        # liste z argumentu dodac do tablicy w ten sposob aby pozostala jednoelementowa
        for item in seq:
            self.append(item)

a1 = DynamicArray()
b = ["pies", 8]
c = [2,4,5,6,7,8]
a1.append(b)
a1.append(c)
a1.extend(c)
print(a1.__getitem__(0))
print(a1.__str__())
print(a1.__str__())
