class HashTable:
    def __init__(self, size, function, method):
        self.size = size
        if method == "chaining":
            self.table = [[] for _ in range(self.size)]
        else:
            self.table = [None] * self.size
        self.function = function
        self.method = method

    def hash_function(self, key):
        """Zastosowanie funkcji haszującej"""
        return self.function(key) % self.size

    def insert(self, key, second_function=None):
        """Wstawianie klucza do tablicy"""

        if self.method == "chaining":
            index = self.hash_function(key)
            if key not in self.table[index]:
                self.table[index].append(key)

        elif self.method == "linear_probing":
            index = self.hash_function(key)
            start_index = index

            while self.table[index] is not None and self.table[index] != key:
                index = (index + 1) % self.size
                if index == start_index:
                    raise Exception("Hash table is full")

            if self.table[index] is None:
                self.table[index] = key

        elif self.method == "second_hashing_function":
            if second_function is None:
                raise ValueError("Second function must be provided for double hashing")

            index = self.hash_function(key)
            start_index = index
            i = 0

            while self.table[index] is not None and self.table[index] != key:
                i += 1
                index = (self.hash_function(key) + i * second_function(key)) % self.size
                if index == start_index:
                    raise Exception("Hash table is full")

            if self.table[index] is None:
                self.table[index] = key

    def display(self):
            print(self.table)


def h(i):
    return 3 * i + 5

keys = [12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5]

hash_table = HashTable(11, h, "chaining")

def hashing():
    for j in keys:
        hash_table.insert(j)
        hash_table.display()


