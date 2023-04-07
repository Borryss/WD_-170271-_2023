
import numpy as np
import math

z = np.arange(7,13).reshape(2,3)


for i in range(0,2):
    b = math.cos(z[i,0])
    print(b,"\n")
    b = math.cos(z[i,1])
    print(b,"\n")
    b = math.cos(z[i,2])
    print(b,"\n")








