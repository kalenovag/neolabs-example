# import math
# import math as m #импорт с переименованием
# print("значение е", m.e)

# from math import *
# print(e, pi, tau, cos(0.12))

# import random
# com = random.randint(1,100)
# while True:
#     user = int(input("введите ваше предсказание: "))
#     if com == user:
#         print("вы угадали, число", com)
#         break
#     elif com > user:
#         print("слишком мало!")
#     else:
#         print("слишком много!")

import random
moves = ["rock", "paper", "scissors"]
com_win = 0
user_win = 0
while com_win !=3 and user_win !=3:
    com = random.choice(moves)
    user = input("введите выбор: ")
    print(f"компьютер выбрал {com}, вы выбрали {user}")
    if com == "rock" and user == "scissors":
        com_win += 1
    elif com == "scissors" and user == "paper":
        com_win += 1
    elif com == "paper" and user == "rock":
        com_win += 1

    elif com == "rock" and user == "paper":
        user_win += 1
    elif com == "paper" and user == "scissors":
        user_win += 1
    elif com == "scissors" and user == "rock":
        user_win += 1

    print(f"Ком: {com_win}, пользователь: {user_win}")

if user_win > com_win:
    print("пользователь победил!")
else:
    print("компьютер победил")

