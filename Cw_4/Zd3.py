
import numpy as np


def fun1(n):
    l = np.arange(1, n*n)
    return l


m = eval(input("Wpisz liczbe"))

print(fun1(m), "\n")
print(fun1(m).shape)








