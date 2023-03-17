
import numpy as np

def fun1(n,m):
    k = np.logspace(1, m, num=m, base=n, dtype='int64')
    print(k)


n = eval(input("Wpisz 1 liczbe"))
m = eval(input("Wpisz 2 liczbe"))

fun1(n,m)


