import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,21)

plt.plot(x, 1/x,   label ='f(x)= x/1')
plt.axis([0,20,0,1])
plt.ylabel('x')
plt.xlabel('f(x)')
plt.legend(loc=1)
plt.show()



