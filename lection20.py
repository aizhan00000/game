# file = open('fiile.txt', 'w')
# file.write('Hello, world!')
# file.close()

# file = open('Name.txt', 'r')
# print(file.read())
# file.close()

# string = 'asdfsagas'
# file = open('Name.txt', 'a')az
# file.write(string)
# file.close()

# username = input('Enter a username: ')
# email = input('Enter an email: ')
# password = input('Enter a password: ')
# password2 = input('Repeat a password: ')
# while password != password2:
#     print('Passwords not match! Try again')
#     password = input('Enter a password: ')
#     password2 = input('Repeat a password: ')
# else:
#     file = open('users.csv', 'w')
#     string = username + ',' + email + ',' + password
#     file.write(string)
#     file.close()


# file = open('Books.csv', 'w')
# string_1 = 'To Kill A Mockingbird,Harper Lee,1960'
# string_2 = 'A Brief History of Time,Stephen Hawking,1988'
# string_3 = 'The Great Gatsby,F. Scott Fitzgerald,1922'
#
# file.write(string_1)
# file.write(string_2)
# file.write(string_3)
# file.close()
#
# my_list = [string_1, string_2, string_3]
# for i in my_list:
#     file.write(i + '\n')
# file.close()

# file = open('Books.csv', 'a')
# new_string = input('Enter string like s,s,s: ')
# file.write(new_string)
# file.close()
#
# file = open('Books.csv', 'r')
# print(file.read())
# file.close()

# import csv
#
#
# how_many_to_add = int(input("Enter count of records to add: "))
# count = 0
# file = open('Books.csv', 'a')
# while count != how_many_to_add:
#     count += 1
#     record = input("Enter a string like s,s,d: ")
#     file.write('\n' + record)
# file.close()
#
# author_name = input("Enter an Author: ")
# file = list(csv.reader(open('Books.csv')))
# print(file)
# for row in file:
#     if author_name in str(row):
#         print(row)

# file = open('Books.csv','r')
# for row in file:
#     if 'Stefen' in row:
#         print(row)


# import csv
#
#
# file = list(csv.reader(open('Books.csv')))
# start = int(input("Enter a 1st year: "))
# stop = int(input("Enter a 2nd year: "))
# for row in file:
#     for i in range(start, stop):
#         year = str(i)
#         if year in row:
#             print(row)


# file = open('Books.csv', 'r')
# start = int(input("Enter a 1st year: "))
# stop = int(input("Enter a 2nd year: "))
# for row in file:
#     for i in range(start, stop):
#         year = str(i)
#         if year in str(row):
#             print(row)


# import csv
#
# file = list(csv.reader(open('Books.csv')))
# i = [i for i in range(1, len(file))]
# for row in file:
#     for x in i:
#         row.insert(0, x)
#     print(row)

# import csv
#
# file = list(csv.reader(open('Books.csv')))
# print(file)
# counter = 0
# for row in file:
#     counter += 1
#     row.insert(0, str(counter))
#     print(row)

# file = open('Books.csv', 'r')
# counter = 0
# for row in file:
#     counter += 1
#     print(str(counter) + ',' + row)