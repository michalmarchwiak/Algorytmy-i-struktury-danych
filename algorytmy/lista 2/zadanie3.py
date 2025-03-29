
def gmaxmin(s):
    def max1(s):
        if len(s) == 1:
            return s[0]
        else:
            return max(s[0], max1(s[1:]))
    def min1(s):
        if len(s) == 1:
            return s[0]
        else:
            return min(s[0], min1(s[1:]))
    return max1(s) , min1(s)


l=[]

for i in range(int(input("Podaj długość listy:"))):
    l.append(int(input("Podaj liczbę:")))

print("Największa i najmniejsza liczba w liście to:" , gmaxmin(l))