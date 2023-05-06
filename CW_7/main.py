import numpy as np
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt

lista = pd.read_excel('wdd/imiona.xlsx')
print(lista)

# Zad 1

liczb = lista.groupby('Rok')['Liczba'].sum()
print(liczb)
rok = lista['Rok'].unique()
print(rok)

plt.plot(rok, liczb)
plt.show()

# Zad 2

a = lista.groupby('Plec')['Liczba'].sum()
print(a)

a.plot.bar()
plt.show()

# Zad 3

urodz = lista.groupby(['Rok', 'Plec'])['Liczba'].sum().tail(10)
print(urodz)

urodz.value_counts().plot(kind='pie', colors=['green', 'black'], title='Black - chlopaki, Green - dziewczyny')
plt.show()

# Zad 4

zamowienia = pd.read_csv('wdd/zamowienia.csv', sep=';')
print(zamowienia)

sprzedawca = zamowienia.groupby('Sprzedawca')['idZamowienia'].count()
print(sprzedawca)

sprzedawca.plot.bar()
plt.show()






