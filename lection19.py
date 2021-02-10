# class CLassName:
# #     a = 5
# #     b = 5
# #
# #     def __init__(self, hp):
# #         self.hp = hp
# #
# #     def __del__(self):
# #         print("IAS")
# #
# #     def print_hp(self):
# #         print(self.hp)
# #         print(self.a)
# #
# #
# # class ClassName2(CLassName):
# #     def print_hp(self):
# #         print(self.a)
# #
# # ''
# # a = CLassName(10)
# # print(a.hp)
# # a.print_hp()
# # del a
# #
# # b = ClassName2(90)
# # print(b.b)
# # b.print_hp()

#
# class A:
#     a = 10
#
#     def __init__(self, name, country, grade, age):
#         self.name = name
#         self.grade = grade
#         self.country = country
#         self.age = age
#
#
# class B:
#     b = 15
#
# class C:
#     a = 50
#     c = 90
#
# class D(C, B, A):
#     def __init__(self, surname,  *args):
#         super().__init__(*args)
#         self.surname = surname
#
#
#     def some_method(self, some_arg):
#         print(some_arg)
#
# d = D('Name', "Surname", 1, 11, 'ojd')
# print(d.name)
# print(d.age)
#
# d.some_method(10)


def sum_nums(a, b):
    return a + b


def minus(a, b):
    return a - b


def div(a, b):
    return a / b


def multiply(a, b):
    return a * b


def main():
    counter = 0
    file = open('resultd.csv', 'a')
    while answer == 'y':
        counter +=1
        file = open('resultd.csv', 'a')
        try:

            a, b = input("enter 2 nums with ',' :  ").split(',')
            a, b = int(a), int(b)
            user_choice = input("Choose * / + - : ")
            file.write(f'Result {counter},')
            if user_choice == '+':
                sum_num = (sum_nums(a, b))
                file.write(str(sum_num))
            if user_choice == '-':
                minus_num = (minus(a, b))
                file.write(str(minus_num))
            if user_choice == '*':
                multiply_num = (multiply(a, b))
                file.write(str(multiply_num))
            if user_choice == '/':
                div_num = (div(a, b))
                file.write(str(div_num))
        # file.write(',')
        except TypeError:
            print("There is a mistake in your code ")

        finally:
            file.write(',')
            file.close()

        answer = input("continue y/n:  ").lower()


main()





