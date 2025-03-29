
def mul(n,m):
    if m == 0:
        return 0
    else:
        return n + mul(n,m-1)

a = int(input("Pierwszy czynnik to:"))
b = int(input("Drugi czynnik to:"))
print("Wynik mnożenia to:" , mul(a, b))