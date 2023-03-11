
import random

random.seed()
def multipli_game():
    poprawna = 0
    niepoprawna = 0
    arik = []
    for i in range(1, 11):
        print("Pytanie ", i ,": ", end = '')
        b = random.randint(1, 9)
        c = random.randint(1, 9)
        a = eval(input(str(b) + " x " + str(c) + " ="))
        if (b*c == a):
            print("Poprawna odpowiedz!")
            poprawna += 1
        else:
            print("Bledna odpowiedz,poprawna odpowiedzia jest " + str(b*c))
            niepoprawna +=1
    arik.append(niepoprawna)
    arik.append(poprawna)
    return arik      
            
            
arfik= multipli_game()
print("Koniec gry!")            
print("Bledne odpowiedzi: ", arfik[0])
print("Poprawne odpowiedzi: ", arfik[1])





