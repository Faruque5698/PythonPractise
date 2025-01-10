import random

upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

print('Welcome to most secure password generator!')

my_upper = int(input('How many upper case your want to use? \n'))
my_lower = int(input('How many lower case your want to use? \n'))
my_number = int(input('How many number your want to use? \n'))
my_symbol = int(input('How many symbol your want to use? \n'))

password_list = []

for upper in range(0,my_upper):
    password_list += upper_case[upper]

for lower in range(0,my_lower):
    password_list += lower_case[lower]

for number in range(0,my_number):
    password_list += numbers[number]

for symbol in range(0,my_symbol):
    password_list += symbols[symbol]

print(password_list)

random.shuffle(password_list)
print(password_list)

password = ''
for char in password_list:
    password += char

print("Generate Password:",password)