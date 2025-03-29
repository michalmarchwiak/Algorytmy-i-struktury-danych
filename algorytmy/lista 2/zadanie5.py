

def palindrom(word):
    word = word.lower()
    if len(word) == 1 or len(word) == 2:
        return word[0] == word[-1]
    elif len(word) == 3:
        return word[0] == word[-1]
    else:
        return palindrom(word[1:-1])


slowo = input("Podaj słowo:")
if palindrom(slowo):
    print(slowo , "jest palindromem")
else:
    print(slowo, "nie jest palindromem")

print(palindrom(slowo))