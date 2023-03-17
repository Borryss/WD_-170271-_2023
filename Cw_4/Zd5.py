
import numpy as np

def fun1(n):

    l = np.arange(n, 0, -1)
    k = np.diag([a for a in l], 0)
    print(k)


m = eval(input("Wpisz liczbe"))

fun1(m)












