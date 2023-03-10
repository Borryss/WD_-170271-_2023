import random


def guess_the_number(a):
    liczba = 0
    random.seed()
    b = random.randint(1, 10)
    if(a == b):
        liczba += 10

    else:
        liczba -= 1

    return liczba


for i in range (1, 5):
    a = eval(input("Zgad liczbę: "))
    if (a in range (1, 10)):
        print(guess_the_number(a))
    else:
        while(a not in range(1, 10)):
            a = eval(input("Zgad liczbę: "))
        print(guess_the_number(a))

