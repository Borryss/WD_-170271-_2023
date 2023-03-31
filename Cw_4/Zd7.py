
import numpy as np

def fun1(n):
    a = np.ones(n, dtype=int)*2
    b = np.diag(a)

    for i in range (1,n):
        x = np.ones(n-i, dtype=int)*2*(i+1)
        b += np.diag(x,i) + np.diag(x,-i)


    print(b)

n = int(input("Wpisz wymiar macierzy: "))
fun1(n)