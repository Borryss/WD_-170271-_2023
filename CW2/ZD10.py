
# Online Python - IDE, Editor, Compiler, Interpreter

x = eval(input("Napisz liczbe od 1 do 10: "))
if x in range(1, 11):
    for i in range(1, x + 1):
        for j in range(1, 11):
            if (j <= i):
                print("H", end='')
            else:
                print("")
                break

else:
    print("Spropuj ponuwnie")
        
    