
# Online Python - IDE, Editor, Compiler, Interpreter

import random


liczba = 0

def guess_the_number(a, liczba):
    
    random.seed()
    b = random.randint(1, 10)
    if(a == b):
        liczba = liczba + 10

    else:
        liczba = liczba - 1

    return liczba


for i in range (1, 6):
    a = eval(input("Zgad liczbę: "))
    if(i == 5 ):
        print("Twoja liczba punktow to: ", guess_the_number(a,liczba))
        liczba = guess_the_number(a,liczba)
        
    elif (a in range (1, 10)):
        print(guess_the_number(a,liczba))
        liczba = guess_the_number(a,liczba)
        
    else:
        while(a not in range(1, 10)):
            a = eval(input("Zgad liczbę: "))
        print(guess_the_number(a,liczba))
        liczba = guess_the_number(a,liczba)
        
        