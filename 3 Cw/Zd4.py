
def funkcja1(a =1, r = 1, ile = 10):
    i = 0
    suma = 0
    while(i < ile):
        suma += a + (r * i)
        i += 1
    return suma


a = eval(input("Wpisz wartość początkowa: "))
b = eval(input("Wpisz wielkość o ilerosną kolejne elementy: "))
c = eval(input("Wpisz ile elementów ma sumować: "))
print("Suma dowolnego ciągu arytmetycznego to ", funkcja1(a,b,c))



