def sumka(l):
    suma = 0
    for i in range(len(l)):
        for j in range(len(l[i])):
            suma += l[i][j]
    return suma

a = [[1,2,3],[4,5,6],[7,8,9]]
print(sumka(a))
