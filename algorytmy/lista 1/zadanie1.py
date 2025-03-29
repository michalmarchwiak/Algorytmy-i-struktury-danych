1.1
### Pierwszy algorytm o klasie O(n^2), 1 - iterowanie, 2 - potęgowanie

def alg1(a,x,n):
    sum = 0
    for i in range(n):
        sum += a[i] * (x ** i)
    return sum

1.2
### Funkcja usprawniająca potęgowanie

def power(x,n):
    if n == 0:
        return 1
    else:
        return x * power(x,n-1)

### Drugi algorytm usprawniony o funkcję przyspieszającą potęgowanie

def alg2(a,x,n):
    sum = 0
    for i in range(n):
        sum += a[i] * power(x,i)
    return sum

("p(x) = a0 + x(a1 + x(a2 + x(...(an-1 + x*an)...))),"
 "patrzymy się na poczxątek na najwyzszy wsp. potem przechodzimy sobie od przedostatniego do pierwszego(a0) idąc wstecz mnozymy nasz wyraz przez x i dodajemy do tego nastepny wsp.."
 "Czyli na kadym 'kroku' robimy 2 operacje. Czyli w sumie nasza liczba operacji wynosi 1(patrzymy na ostatni) + 2(liczba operacji na kazdym kroku)(n-1)(liczba kroków) = 2n-1 czyli O(n) ")
