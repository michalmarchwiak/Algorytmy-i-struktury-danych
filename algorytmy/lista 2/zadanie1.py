
def fmax(s):
    if len(s) == 1:
        return s[0]
    else:
        return max(s[0],fmax(s[1:]))

l=[]

for i in range(int(input("Podaj długość listy:"))):
    l.append(int(input("Podaj liczbę:")))

print("Największa liczba w podanej liście to:" ,fmax(l))