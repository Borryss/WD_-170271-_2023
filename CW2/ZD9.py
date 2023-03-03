lista = []
liczba = input("Napisz liczbe")
while liczba != "end":
    x = liczba.isdigit()
    if x:
        lista.append(liczba)
    liczba = input("Napisz liczbe")
print(lista)

