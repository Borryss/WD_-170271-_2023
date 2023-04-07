import numpy as np
import math

b = np.arange(1,7).reshape(2,3)

print(b[0,0])

for i in range(0,2):
    a = math.sin(b[i,0])
    print(a,"\n")
    a = math.sin(b[i,1])
    print(a,"\n")
    a = math.sin(b[i,2])
    print(a,"\n")