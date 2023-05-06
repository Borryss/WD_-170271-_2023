import numpy as np
import matplotlib.pyplot as plt
import openpyxl
import pandas as pd
import random

zb_danych = pd.read_csv('wdd/iris.data', header = None, names = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class'])
print(zb_danych)

data ={'sepal length':zb_danych['sepal length'], 'sepal width':zb_danych['sepal width'], 'c':np.random.randint(0, 150, 150), 'd':np.abs(zb_danych['sepal length'] - zb_danych['sepal width'])}
plt.scatter('sepal length', 'sepal width', c='c', s='d', data=data)
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.show()