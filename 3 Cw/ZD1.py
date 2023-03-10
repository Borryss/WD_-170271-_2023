def funkcja1(a):
    if(a > 0):
        return ("Funkcja rosnąca ")
    elif(a<0):
        return ("Funkcja malejąca")
    else:
        return ("Funkcja stała" )

a = eval(input("Wpisz wartosc a: "))
print(funkcja1(a))