l = []
for i in range(10000000000000):
    l.append(i)


def example1(S):
    n = len(S)
    total = 0
    for j in range(n):
       total += S[j]
    return total
print(example1(l))

print("hello world")