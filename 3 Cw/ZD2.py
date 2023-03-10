def funkcja1(a1, a2):
    if(a1 == a2 and (a1*a2) != -1):
        return ("Prosta są równoległa")
    elif((a1*a2) == -1 and a1 != a2):
        return ("Prosta są prostopadła")
    elif((a1*a2) == -1 and a1 == a2):
        return ("Prosta są prostopadła oraz równoległa")
    else:
        return ("Prosta ")





a1 = eval(input("Wpisz a1: "))
a2 = eval(input("Wpisz a2: "))
print(funkcja1(a1, a2))
