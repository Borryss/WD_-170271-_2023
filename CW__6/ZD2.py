import pandas as pd
import numpy as np
import openpyxl

lista = pd.read_excel("wdd/imiona.xlsx")


#a)

a = lista[lista['Liczba'] > 1000]
print(a, "\n")



#b)

b = lista[lista['Imie'] == "BORYS"]
print(b, "\n")


#c)

c = lista['Liczba'].sum()
print(c, "\n")

#d)

d = lista.groupby(['Rok']).sum(['Liczba'])
print(d, "\n")

#e)
e = lista.loc[(lista['Rok'] >= 2000) & (lista['Rok'] <= 2005)]['Liczba'].sum()
print(e,"\n")

#f)
f = lista.groupby(['Plec'])['Liczba'].sum().reset_index()
print(f,"\n")


#g)


sum = lista.groupby(['Plec', 'Imie'])['Liczba'].sum().reset_index()

g = sum.loc[sum.groupby(by='Plec')['Liczba'].idxmax()]['Imie']
print(g,"\n")

#h)

suma_zarok = lista.groupby(['Plec', 'Imie', 'Rok'])['Liczba'].sum().reset_index()
print(suma_zarok,"\n")

h = suma_zarok.loc[suma_zarok.groupby(by=['Rok', 'Plec'])['Liczba'].idxmax()]
print(h,"\n")