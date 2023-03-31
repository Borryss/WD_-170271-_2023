
import numpy as np

def fun1(a, kier = 0):
    if (kier == 1 and a.shape[1] % 2 == 0):
        half = a.shape[1]//2
        new_a1 = a[:, :half]
        new_a2 = a[:, half:]
        print("Pierwsza pulowa to: \n",new_a1,"\n","Druga pulowa to: \n", new_a2, "\n")
    elif(kier == 0 and a.shape[0]%2 == 0):
        half = a.shape[0]//2
        new_a1 = a[:half]
        new_a2 = a[half:]
        print("Pierwsza pulowa to: \n",new_a1,"\n","Druga pulowa to: \n", new_a2, "\n")
    else:
        print("Nie da sie")

tab = np.arange(1,17)
tab = tab.reshape(4,4)
fun1(tab,1)







