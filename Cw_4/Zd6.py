
import numpy as np

def foo6():
    slowo1 = "mleko"
    slowo2 = "maslo"
    slowo3 = "obcios"
    slowo3_1 = slowo3[::-1]
    print(slowo3_1)
    maciez = np.zeros((5,6),dtype=str)
    maciez[:,0] = np.fromiter((slowo1), dtype="S1")
    maciez[4:,::-1] = np.fromiter((slowo3_1), dtype="S1")
    np.fill_diagonal(maciez,list(slowo2))
    print(maciez)


print(foo6())













