import numpy as np
import math

g = np.arange(1,7).reshape(2,3)

print(g[0,0])

for i in range(0,2):
    a = math.sin(g[i,0])
    print(a,"\n")
    a = math.sin(g[i,1])
    print(a,"\n")
    a = math.sin(g[i,2])
    print(a,"\n")

z = np.arange(7,13).reshape(2,3)


for i in range(0,2):
    b = math.cos(z[i,0])
    print(b,"\n")
    b = math.cos(z[i,1])
    print(b,"\n")
    b = math.cos(z[i,2])
    print(b,"\n")


print(a+b)





