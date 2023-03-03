# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# ZD1
new_var = input("Please enter some text  ")
print(new_var.count(" "))

# ZD2
nazwa = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz " \
        "pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później " \
        "zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w " \
        "latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z " \
        "zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach " \
        "osobistych, jak Aldus PageMaker "


print(nazwa.split(), type(nazwa))

# ZD3
Link_na_dokumentacje = "https://www.w3schools.com/python/python_conditions.asp"

# ZD4
liczba1 = eval(input("Liczba to:"))
print(abs(liczba1))

# ZD5
liczba2 = [1, 2, 3]
for i in [1, 2, 3]:
    liczba2[i - 1] = eval(input("Napisz liczbe: "))
    if liczba2[i - 1] in range(1, 11):
        print("Liczba jest od 1 do 10")
if liczba2[0] > liczba2[1]:
    print("Liczba a > b")
elif liczba2[1] > liczba2[2]:
    print("Liczba b > c")

# ZD6
for i in range(51):
    if i % 5 == 0:
        print(i)




# ZD7
liczba3 = input("Wpisz ilosc liczb: ").split(" ")
for liczba3 in liczba3:
    print(int(liczba3)*int(liczba3))

















