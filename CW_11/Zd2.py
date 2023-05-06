import numpy as np
import matplotlib.pyplot as plt

np.random.seed()
series = np.random.rand(5, 50)

col = ['r', 'b', 'g', 'y', 'm']
mark = ['o', '^', 's', 'D', 'v']

def fun1(n,vmin,vmax):
    return (vmax - vmin) * np.random.rand(n) + vmin

fg = plt.figure()
ax = fg.add_subplot(111, projection='3d')
n = 50
for i in range(5):
    xs = fun1(n, 0, 50)
    ys = fun1(n, 0, 50)
    ax.scatter(xs, ys, series[i], c=col[i], marker=mark[i])

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()




