import numpy as np
import matplotlib.pyplot as plt
import openpyxl
import pandas as pd
import random

zamowienia = pd.read_csv('wdd/zamowienia.csv', sep=';')
print(zamowienia)

sprzed = zamowienia['Sprzedawca'].unique()
sprzed.sort()
sum_zam = zamowienia.groupby('Sprzedawca')['Utarg'].sum()

plt.pie(sum_zam, labels=sprzed, autopct=lambda pct:"{:.1f}%".format(pct), textprops=dict(color="black"))
plt.show()