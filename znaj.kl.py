from random import randint
from math import sqrt

GAME_WITH = 10
GAME_HEIGHT = 10
key_x = randint(0,GAME_WITH)
key_y = randint(0,GAME_HEIGHT)
player_x = 0
player_y = 0
steps = 0
player_found_key = False

print(key_x,key_y)
distance_before_move = sqrt((key_x - player_x)**2 + (key_y - player_y)**2)
while not player_found_key:
    steps +=1
    print()
    print("Może udać się w określonych kierunkach jako [W/A/S/D]")

    move = input("Skąd idziesz?")
    match move:
        case "W":
            player_y += 1
            if player_y > GAME_WITH:
                print("Ach!! ty uderzasz w ścianie.")
                player_y = GAME_WITH
        case "S":
            player_y -= 1
            if player_y < 0:
                print("Ach!! ty uderzasz w ścianie.")
                player_y = 0
        case "A":
            player_x -= 1
            if player_x < 0:
                print("Ach!! ty uderzasz w ścianie.")
                player_x = 0
        case "D":
            player_x += 1
            if player_x > GAME_WITH:
                print("Ach!! ty uderzasz w ścianie.")
                player_x = GAME_WITH
        case "Q":
            print("Koniec gry")
            quit()
        case "_":
            print("Nie wiem dokąd ty idziesz..")
            continue
    if(player_x == key_x and player_y == key_y):
        print("Good!!Znalazleś klucz")
        print(f"Wykonałeś {steps} kroków")
        quit()

    distance_after_move = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)
    print("before",distance_before_move)
    print("after",distance_after_move)
    if distance_before_move > distance_after_move:
        print("Cieplej")
    else:
        print('Zimnej')
    distance_before_move = distance_after_move
    print(player_x, player_y)