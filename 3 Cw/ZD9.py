



a = eval(input("Podaj nie parzysta wysokosc A:"))
if (a%2 == 0):
    print("Liczba musze byc nie parzysta")
    
else:
    b = int((a+1)/2)
    for i in range(1, a+1):
        if (i == b):
            print((" "*(a-b))+("*" *(a))+(" "*(a-b)))
        elif(i == 1):
            print((" "* (a-i))+"*"+ (" "* (i -1)) + (" "* (a-i)))
        else:
            print((" "* (a-i))+"*"+ (" "* (2*i -3 ))+ "*" + (" "* (a-i)))
    



    



