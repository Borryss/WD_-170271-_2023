import numpy as np
import matplotlib.pyplot as plt
import openpyxl
import pandas as pd
import random

def fun1(n):
    list = []
    while(n > 0):
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        suma = d1 + d2
        print(d1, d2)
        list.append(suma)
        n -= 1
    return list

n = 7
x = fun1(n)
print(x)

plt.hist(x, bins=n, color='g', alpha=1, density=True)
plt.xlabel('Wartosc')
plt.ylabel('Prawdopodobienstwo')
plt.title('Histogram rzucania')
plt.grid(True)
plt.show()