
# a = [1, 2, 3, 4, 7, 9, 10.10, 23.7, 6, 9, 0]
# print(a)
# b = []
# for i in a:
#     i += 5
#     b.append(i)
# print(b)
# a.clear()
# for i in b:
#     a.append(i)
# b.clear()
# print(a)
# # print(b)


# a = [[i for i in range(0, 5)]for i in range(0, 3)]
# print(a)
#
# i = 0
# while i < 10:
#     print(i)
#     i += 3


# a = [i for i in range(0, 11)]
# print(a)
# length = len(a)
# print(length)
# i = 0
# b = []
# while i < length:
#     res = a[i] * 2
#     i += 1
#     b.append(res)
# print(b)

# name = input("enter your name: ")
# for i in range(0, 3):
#     print(name)


# name = input("enter your name:  ")
# num = int(input("enter your num:  "))
# for i in range(0, num):
#     print(name)

# name = input("enter your name:  ")
# for i in name:
#     print(i)

#
# name = input("enter your name:  ")
# num = int(input("enter your num:  "))
# for i in range(0, num):
#     for j in name:
#         print(j)

# num = int(input("Enter ypur num:   "))
# for i in range(0, 10):
#     print(f'{num} x {num} =', num * i)

# num = int(input("enter ypur num below 50:  "))
# for i in range(50, num, -1):
#     print(i)

# name = input("enter your name:  ")
# num = int(input("enter your num below 10:  "))
#
# if num <= 10:
#     for i in range(0, num):
#         print(name)
#     else:
#         print("too high " * 3)

# total = 0
# for i in range(0, 5):
#     a = int(input("enter a num:  "))
#     ans = input("do ypu want to include it> (y/n) ")
#     if ans == 'y':
#         total += a
#         print('you didn\'t include the num')
# print(total)

#
# total = 0
# statement = 0
# while True:
#     a = int(input("enter a num:  "))
#     ans = input("do you want to include it? (y/n)")
#     if ans == 'y':
#         statement += 1
#         if statement == 5:
#             break
#         else:
#             print("you didnt include a num")
#
# print(total)


# login = input("enter your login:  ")
#
# while True:
#     password = input("enter yout pw:  ")
#     char = password[0]
#     if char.isupper():
#         break
# print(password)


# ans = input("Up or down? (y/n) ").lower()
# if ans == 'up':
#     num = int(input("enter a top of numbers:  "))
#     for i in range(1, num):
#         print(i)
# else:
#     num = int(input("enter a num below 20: "))
#     for i in range(20, num, -1):
#         print(i)

# people = int(input("how many people do you want to i clude:  "))
# if people < 10:
#     for i in range(0, people):
#         name = input("enter a name:  ")
#         print("{} has been invited".format(name))
# else:
#     print("too many people")



