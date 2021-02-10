# import random
#
#
# def rps(user1, user2):
#     beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
#     if beats[user1] == user2:
#         return "User won!"
#     elif beats[user2] == user1:
#         return "Computer won!"
#     else:
#         return "Tie"
#
# def player(choices: list):
#     while True:
#         choices = ['rock', 'scissors', 'paper']
#         user_choice = int(input("Rock=0, Scissors=1, Paper=2\nEnter num from 0 to 2: "))
#         user = choices[user_choice]
#
#         com = random.choice(choices)

#         print("User choose:", choices[user_choice])
#         print("Computer choose:", com)
#
#         print(rps(user, com))
#
#         cont = input("Continue? (y/n) ")
#         if cont.lower() != 'y':
#             print("Game over")
#
# player(['rock', 'scissors', 'paper'])
# print(player)
# print("Game over")


import random

# com = random.choice(['h', 't'])
# user = input("enter h or t:  ").lower()
# if com == user:
#     print("user wins")

# com = random.randint(1, 5)
# user = int(input("enter a num"))
# if com == user:
#     print('well done')
# else:
#     user = int(input("enter another num:  "))
#     if user == com:
#         print("correct!")
#     else:
#         print("you lost!")


# num = random.randint(1, 10)
# user = 0
# while user != num:
#     user = int(input("enter a num between1 and 10:  "))
#     if user > num:
#         print("too high!")
#     else:
#         print("too low")
# else:
#     print("you won")

# num = random.randint(1, 10)
# user = 0
# while user != num:
#     num = random.randint(1, 10)
#     user = int(input("enter a num from 1 to 10:  "))
#     print("comp[ num:   ", num)
#     if user != num:
#         print("try again")
# else:
#     print("you win")

# a = [i for i in range(0, 11)]
# b = random.choice(a)
# print(b)
# if b in a:
#     a.remove(b)
# print(a)

# a = [i for i in range(0, 11)]
# while a:
#     b = random.choice(a)
#     print(b)
#     if b in a:
#         a.remove(b)
#     print(a)


# a = ['aijan', 'adilet', 'edil', 'dinislam', 'aigul']
#
#
# while a:
#     user = input("continue? (y/n) ")
#     b = random.choice(a)
#     print(b)
#     if b in a:
#         a.remove(b)
#     print(a)


# i = 0
# while i < 5:
#     i += 1
#     a = random.randint(0, 10)
#     b = random.randint(0, 10)
#     c = a + b
#     user = int(input(f'{a} + {b} = '))
#     if user == c:
#         print("you are right")
#     else:
#         print("not true")


# colors = ['red', 'green', 'blue', 'yellow',
#           'white']
# comp = random.choice(colors)
# while True:
#     user = int(input("red=0, green=1, blue=2, yellow=3, white=5,"
#                      "enter a num:  "))
#
#     user = colors[user]
#     if comp == user:
#         print("well done !!!")
#     else:
#         print(f"i bet you are {comp} eith envy")
#         print(f"you are probably feeleing {user} righ now")