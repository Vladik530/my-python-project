a,b,c=map(int,input().split())
mnozenie = a * b * c
print(mnozenie)
dzielenie = a / b / c
print(dzielenie)
dodawanie = a + b + c
print(dodawanie)
odejmowanie = a - b - c
print(odejmowanie)
potengowanie = a ** b ** c
print(potengowanie)
print()
if a > b and a > c:
    print(a)
else:
    print(b,c)
print()
from  random import randint
for i in range(0,10):
    print(randint(0,50))
print()
i = 0
while i<11:
    print(i)
    i+=2
print("koniec")




