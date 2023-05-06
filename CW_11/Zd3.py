import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

fg = plt.figure()
a = fg.add_subplot(projection='3d')
x = np.arange(-5, 5, 0.25)
y = np.arange(-5, 5, 0.25)
x, y = np.meshgrid(x, y)
b = np.sqrt(x ** 2 + y ** 2)
c = np.sin(b)
color = cm.get_cmap('inferno', lut=5)
s = a.plot_surface(x, x, c, cmap=color, linewidth=0, antialiased=False)
a.set_zlim(-1.01, 1.01)
a.zaxis.set_major_locator(LinearLocator(10))
a.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
fg.colorbar(s, shrink=0.5, aspect=5)
plt.show()