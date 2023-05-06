import numpy as np
import matplotlib.pyplot as plt

fg =plt.figure()
a =fg.add_subplot(projection='3d')
b =np.linspace(0,2*np.pi,100)
c =b
x =np.sin(b)
y =2*np.cos(b)
a.plot(x,y,c,label='zadanie 1')
a.legend()
plt.show()

