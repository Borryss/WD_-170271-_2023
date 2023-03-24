
import numpy as np



def foo7(n):
    macierz = np.zeros((n,n),dtype=int)
    for i in range(n):
        for j in range(n):
            if (i==j):
                macierz[i][j]=2
            elif(i+j == n-1):
                macierz[i][j] = 6
            elif (i + j == n or n-2):
                macierz[i][j] = 4

    print(macierz)

foo7(5)



