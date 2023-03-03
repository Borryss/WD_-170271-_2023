# ZD5
liczba2 = [1, 2, 3]
for i in [1, 2, 3]:
    liczba2[i - 1] = eval(input("Napisz liczbe: "))
    if liczba2[i - 1] in range(1, 11):
        print("Liczba jest od 1 do 10")
if liczba2[0] > liczba2[1]:
    print("Liczba a > b")
elif liczba2[1] > liczba2[2]:
    print("Liczba b > c")
