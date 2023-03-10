import math

def funkcja1(a = 3, b = 4):
    c = math.sqrt((a*a) + (b*b))
    return c

a = eval(input("Wpisz a: "))
b = eval(input("Wpisz b: "))
print("Długość przeciwprostokątnej to ", funkcja1(a,b))
