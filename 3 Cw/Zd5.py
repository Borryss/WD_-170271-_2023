lista = ["Ruslan", "kocha", "puszka", "piwa"]

def dodaj_znak_punktb(lista):
    listz = lista
    for i in range (0, len(listz)):
        listz[i] = listz[i].replace(listz[i], listz[i] + "!")
    return listz

print(dodaj_znak_punktb(lista))

lista = ["Ruslan", "kocha", "puszka", "piwa"]

def dodaj_znak_punkta(lista):

    for i in range (0, len(lista)):
        lista[i] = lista[i].replace(lista[i], lista[i] + "!")
    return lista

print(dodaj_znak_punkta(lista))


