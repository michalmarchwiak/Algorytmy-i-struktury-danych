from zadanie1 import HashTable
from zadanie1 import h
keys = [12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5]

def k(i):
    return 7 - (i % 7)

hash_table2 = HashTable(11, h, "second_hashing_function")

def hashing():
    for key in keys:
        hash_table2.insert(key, k)
        hash_table2.display()
