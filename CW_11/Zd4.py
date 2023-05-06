
import numpy as np
import matplotlib.pyplot as plt

fg = plt.figure(figsize=(10, 4))
a1 = fg.add_subplot(421, projection='3d')
a2 = fg.add_subplot(422, projection='3d')
a3 = fg.add_subplot(423, projection='3d')
a4 = fg.add_subplot(424, projection='3d')
a5 = fg.add_subplot(425, projection='3d')
a6 = fg.add_subplot(426, projection='3d')
a7 = fg.add_subplot(427, projection='3d')
a8 = fg.add_subplot(428, projection='3d')

_x = np.arange(4)
_y = np.arange(5)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
top = x + y
bottom = np.zeros_like(top)
width = depth = 1

a1.bar3d(x, y, bottom, width, depth, top, shade=True)
a1.set_title('Wykres zacieniony')
a2.bar3d(x, y, bottom, width, depth, top, shade=False)
a2.set_title('Wykres nie zacieniony')
a3.bar3d(x+1, y+2, bottom, width, depth, top, shade=True, color='black')
a3.set_title('Wykres zacieniony')
a4.bar3d(x+1, y+2, bottom, width, depth, top, shade=False, color='black')
a4.set_title('Wykres nie zacieniony')
a5.bar3d(x, y, bottom, width, depth, top, shade=True, color='g')
a5.set_title('Wykres zacieniony')
a6.bar3d(x, y, bottom, width, depth, top, shade=False, color='g')
a6.set_title('Wykres nie zacieniony')
a7.bar3d(x, y, bottom, width, depth, top, shade=True, color='r')
a7.set_title('Wykres zacieniony')
a8.bar3d(x, y, bottom, width, depth, top, shade=False, color='r')
a8.set_title('Wykres nie zacieniony')
plt.show()