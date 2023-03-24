
import numpy as np

x = 4
z = 7
v = int(z+x/2)
a = np.zeros((x,z), dtype=int)



print(a,"\n")

k = 2

def foo8(a):
    if(k == 1):
        if(z%2 != 0):
            print("Ilosc kolumn nie pozwala na operacje")
            return 0
        print(a[::, 0:(2)])

    if(k == 2):
        if (x % 2 != 0):
            print("Ilosc wierszy  nie pozwala na operacje")
            return 0
        print(a[0:(2),::])



foo8(a)










