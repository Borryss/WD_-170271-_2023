
def funkcja1(a):
    counter = 0
    for i in a:
        counter += int(i)
        
        
    return counter
  
a = str(eval(input("Wpisz liczbę: ")))
while(funkcja1(a) > 10 ):
    
    a = str(funkcja1(a))
    (funkcja1(a))
print(funkcja1(a))





