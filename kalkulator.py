print("---Prosty Kalkulator---")
a = int(input("Podaj pierwszą liczbe:"))
b = int(input("Podaj drugą liczbę:"))
while True:
    print("Wybierz opcje:")
    print("1-dodawanie")
    print("2-odejmowanie")
    print("3-mnozenie")
    print("4-dzielenie")
    wybor = int(input("Wybierz opcje:"))
    if wybor == 1:
        print(a + b)
    elif wybor == 2:
        print(a - b)
    elif wybor == 3:
        print(a * b)
    elif wybor == 4:
        if b == 0:
            print("Nie można dzielić prze zero!!!")
        else:
            print(a / b)
    else:
        print("Nie ma takiej opcji!!!")
        break
