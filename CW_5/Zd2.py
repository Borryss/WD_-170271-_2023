import numpy as np
import random as rd

rd.seed()
a = np.random.randint(10,high=51, size=(3,3))
b = np.random.randint(10,high=51, size=(4,4))


print(a,"\n")
print(b,"\n")

print("Najnizsze wartosci dla kazdej kolumny z 1 macierzy",a.min(axis=0),"\n")
print("Najnizsze wartosci dla kazdego rzedu z 1 macierzy",a.min(axis=1),"\n")

print("Najnizsze wartosci dla kazdej kolumny z 1 macierzy",b.min(axis=0),"\n")
print("Najnizsze wartosci dla kazdego rzedu z 1 macierzy",b.min(axis=1),"\n")

