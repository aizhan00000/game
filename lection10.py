# def user_num():
#     num = int(input("enter a num:  "))
#     return num
#
#
# def main(a):
#     for i in range(1, a+1):
#         print(i)
#
#
# main(user_num())

# def user_num():
#     num = int(input("enter a num:  "))
#     return num
#
#
# def main(a):
#     print([i for i in range(1, a+1)])
#
#
# main(user_num())


# def user_num():
#     import random
#     low = int(input("enter a low num: "))
#     high = int(input("enter a high one:  "))
#     comp_num = random.randint(low, high)
#     return comp_num
#
#
# def kkk():
#     print("i am thinking of a number...")
#     user_choice = int(input("what is that num:  "))
#     return user_choice
#
#
# def main():
#     a = user_num()
#     b = kkk()
#     if a == b:
#         return "you win!"
#     else:
#         while True:
#             main()

# print(main())


def num():
    print(
        "1:  Addition\n",
        "2:  Subtraction\n",
        "enter 1 or 2:  "
    )


def number():
    b = int(input('enter a num:  '))
    return b


def main():
    import random
    a = number()
    if a == 1:
        x = random.randint(("5", "20"))
        return x
    elif a == 2:
        g = random.randint(i for i in range(1, 20))
    elif a == 10:
        print("aijan, ty krasivays")
    else:
        print("aijan ty loh")


main()







