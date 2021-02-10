# def my_func():
#     print("Hi")
#
# my_func()
#
# def my_function(fname):
#   print(fname + " Refsnes")
#
# text = 'Email'
#
# my_function(text)
# my_function("Tobias")
# my_function("Linus")
#
#
# def sum_nums(a, b):
#     print(a + b)
#
# sum_nums(3, 5)
#
#
# def sum_nums(a, b):
#     return a + b
#
#
# res = sum_nums(3, 5)
# print(res)
#
# def my_function(*kids):
#   print("The youngest child is " + kids[2] + ' ' + kids[0])
#
# my_function("Emil", "Tobias", "Linus")
#
# def my_function(a, b, c):
#   print("The youngest child is " + a + ' ' + c)
#
#
# num = '3'
# my_function(b="1", c=num, a='2')
#
# def my_function(**kid):
#   print("His last name is " + kid["lname"])
#
# my_function(fname="Tobias", lname="Refsnes")
#
#
# a = {1: 'Value1', 'key': 'Value2'}
# print(a['key'])
#
#
# def my_function(country="Norway"):
#   print("I am from " + country)
#
# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")
#
# def my_function(food):
#   for x in food:
#     print(x)
#
#
# fruits = ["apple", "banana", "cherry", 'kiwi']
#
# my_function(fruits)


# def my_function(x):
#   return 5 * x
#
#
# print(my_function(3))
# print(my_function(5))
# print(my_function(9))

# def func():
#     pass


#
# def factorial_recursive(n):
#     # Base case: 1! = 1
#     if n == 1:
#         return 1
#
#     # Recursive case: n! = n * (n-1)!
#     else:
#         print('n * (n-1)', n)
#         return n * factorial_recursive(n-1)
#
# print(factorial_recursive(5))

# count = 5
# while count > 0:
#     count -= 1
#     print(count)
#
# print()
#
# def count(n):
#     if n < 0:
#         return 0
#     print(n)
#     return count(n-1)
#
# print(count(5))