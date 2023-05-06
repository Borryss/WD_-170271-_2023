import numpy as np
import matplotlib.pyplot as plt
import openpyxl
import pandas as pd

lista = pd.read_excel('wdd/imiona.xlsx')

a = lista.groupby('Plec')['Liczba'].sum()

plt.subplot(1, 3, 1)
a.plot.bar('K', 'M', color=['red', 'blue'])
plt.ylabel('ilosc')

m = lista[lista['Plec'] == 'M'].groupby(['Rok'])['Liczba'].sum()
k = lista[lista['Plec'] == 'K'].groupby(['Rok'])['Liczba'].sum()
rok = lista['Rok'].unique()

plt.subplot(1, 3, 2)
plt.plot(rok, m, label='Meszczyzny')
plt.plot(rok, k, label='Kobiety')
plt.xlabel('rok')
plt.ylabel('M lub K')
plt.legend(loc=1)

wsl2 = lista.groupby('Rok')['Liczba'].sum()

plt.subplot(1, 3, 3)
wsl2.plot.bar()
plt.xlabel('rok')
plt.ylabel('Liczba')
plt.show()

