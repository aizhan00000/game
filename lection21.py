import re

username = input('Enter a list of the names who was invited to the party: ')

file = open('file.txt', 'w')
string = username
file.write(string)
file.close()