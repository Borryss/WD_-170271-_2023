import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Zad1

lista = pd.read_excel('wdd/imiona.xlsx')
lista_k = lista[lista['Imie'].str[0]=='K']
lista_u = lista_k['Imie'].unique()
print(len(lista_u))

#Zad2

lista = pd.read_excel('wdd/imiona.xlsx')
res = lista.groupby(['Plec', 'Imie'])['Liczba'].sum().reset_index()
k = res[res['Plec']=='K'].reset_index()
lista_max = k['Liczba'].idxmax()
lista_m_i = k.iloc[lista_max]['Imie']
k2 = res[res['Plec']=='M'].reset_index()
lista_max2 = k2['Liczba'].idxmax()
lista_m_i2 = k2.iloc[lista_max2]['Imie']

print(lista_m_i)
print(lista_m_i2)

#Zad3

fig , (ax1 , ax2) = plt.subplots(ncols = 2, figsize = (10, 6))
fig.suptitle("Liczba")
ax1.set_title("Wykres w pandasie")
ax2.set_title("Wykres w seabornie")
lista = pd.read_excel('wdd/imiona.xlsx')
data = lista[(lista['Rok']>=2010) & (lista['Rok']<=2015)]
data_gr = data.groupby('Plec')['Liczba'].sum()
data_gr.plot.bar(ax = ax1)
sns.barplot(data = data, x = 'Plec', y = 'Liczba', estimator = sum, ci = None , ax = ax2)

plt.show()







