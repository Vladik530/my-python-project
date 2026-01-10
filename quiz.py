import json

def show_question(question):
    global point
    print()
    print(question)
    print("a:",question["a"])
    print("b:", question["b"])
    print("c:", question["c"])
    print("d:", question["d"])
    print()

    answer = input("Którą odpowiedz wybierasz?")
    if answer == question["prawidlowa_odpowiedz"]:
        point += 1
        print("To prawidlowa odpowiedz,brawo.Masz", point, "punktów")
    else:
        print("Niestety,to zla odpowiedz.Prawidlowa odpowiedz",question["prawidlowa_odpowiedz"])
point = 0
with open("quiz.json") as json_file:
    question = json.load(json_file)

    for i in range(0, len(question)):
        show_question(question[i])
print()
print("To koniec gry,zdobyta liczba punktów to:"+ str(point) + ".")