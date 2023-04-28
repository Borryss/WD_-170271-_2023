import matplotlib.pyplot as plt
import numpy as np





x1 =np.arange(0.0,30.0,0.01)
x2 =np.arange(0.0,30.0,0.01)
y1 =np.sin(x1)
y2 =np.cos(x2)




plt.plot(x1,y1,'b', label = 'sin(x)')
plt.title('Wykres sin(x) cos(x)')
plt.ylabel('sin(x) cos(x)')
plt.plot(x2,y2,'y',label = 'cos(x)' )
plt.xlabel('x')

plt.legend(loc=1)
plt.show()





