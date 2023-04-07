
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








#g)


