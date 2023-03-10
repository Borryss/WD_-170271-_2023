# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def funkcja1(a):
    if(a > 0):
        return ("Funkcja rosnąca ")
    elif(a<0):
        return ("Funkcja malejąca")
    else:
        return ("Funkcja stała" )

a = eval(input("Wpisz wartosc a: "))
print(funkcja1(a))


