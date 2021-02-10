# def color(a):
#     if a == "red" or a == "red" or a == "RED":
#         print('me too')
#     else:
#         print("nooo")
#
#     # cont = input("do you wanna continue?:  ")
#
#
# user_color = input("enter a color:  ")
# print(color(user_color))

# color = input("enter a color:  ")
# if  color == 'red':
#     print("i like it too")
# elif color == 'Red':
#     print("i like it too")
# else:
#     print(f'i font like {color}')


# rain = input("is it rain?: (y/n) ").lower()
# if rain == 'y':
#     wind = input("is it windy? (y/n) ").lower()
#     if wind == 'y':
#         print("too windy for umvrella")
#     else:
#         print("you should take an umbrella")
# else:
#     print("have a lucky day")


# def points(games):
#     x = int(input("chislo:  "))
#     y = int(input("chislo:  "))
#     if x > y:
#         print("3 points")
#     elif x < y:
#         print('0 points')
#     else:
#         print("1 ")

# x = int(input("chislo:  "))
# y = int(input("chislo:  "))
#
# if x > y:
#     print("3 points")
# elif x < y:
#     print('0 points')
# else:
#     print("1 ")

# def points(games):
#     count = 0
#     for score in games:
#         res = score.split(':')
#         if res[0] > res[1]:
#             count += 3
#         elif res[0] == res[1]:
#             count += 1
#     print(count)
#
#
# # printt()
#
# a = 'hello, neobis.how are  you?'
# b = a.split(' ')
# print(b)
# d = []
# for i in b:
#     c = i.split('e')
#     d.append(c)
# print(d)
#
# e = []
# for i in d:
#     for j in i:
#         e.append(j)
# print(e)

#

a = []
b = []
# for i in range(0, 100):
#     for j in range(0, 19):
#         b.append(j)
#         a.append(b)

a = [[j for j in range(0, 10)] for i in range (0, 10)]
print(a)









