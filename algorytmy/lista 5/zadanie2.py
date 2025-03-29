from zadanie1 import HashTable
from zadanie1 import h
keys = [12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5]

hash_table1 = HashTable(11, h, "linear_probing")



def hashing():
    for key in keys:
        hash_table1.insert(key)
        hash_table1.display()

print(hashing())