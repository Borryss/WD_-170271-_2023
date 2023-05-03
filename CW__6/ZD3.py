import pandas as pd
import numpy as np
import openpyxl


zamowienia = pd.read_csv('wdd/zamowienia.csv', sep=';')


a = zamowienia['Sprzedawca'].unique()
print(a, "\n")

sort = zamowienia.sort_values('Utarg', ascending=False)
b = sort['Utarg'].head(5)
print(b, "\n")

c = zamowienia.groupby('Sprzedawca')['Sprzedawca'].count()
print(c, "\n")

d = zamowienia.groupby('Kraj')['Utarg'].sum()
print(d, "\n")

zarok = zamowienia[(zamowienia['Data zamowienia'] >= '2005-01-01') & (zamowienia['Data zamowienia'] <= '2005-12-31')]
e = zarok[zarok['Kraj'] == 'Polska']['Utarg'].sum()
print(e, "\n")

f = zamowienia[(zamowienia['Data zamowienia'] >= '2004-01-01') & (zamowienia['Data zamowienia'] <= '2004-12-31')]['Utarg'].mean()
print(f, "\n")

g_1 = zamowienia[(zamowienia['Data zamowienia'] >= '2004-01-01') & (zamowienia['Data zamowienia'] <= '2004-12-31')]
g_1.to_csv('wdd/zamowienia_2004.csv', sep=';')
g_2 = zamowienia[(zamowienia['Data zamowienia'] >= '2005-01-01') & (zamowienia['Data zamowienia'] <= '2005-12-31')]
g_2.to_csv('wdd/zamowienia_2005.csv', sep=';')
print(g_1, "\n")
print(g_2, "\n")