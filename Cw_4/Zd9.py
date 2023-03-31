import numpy as np

def fun1(n):
    if (n == 0):
        return 1
    elif (n==1):
        return 1
    else:
        return fun1(n-2) + fun1(n-1)

a = np.arange(0,25)
for i in range(0,25):
    a[i] = fun1(i)
a= a.reshape(5,5)
print(a)






