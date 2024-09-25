#spliting the string
#string = ['abcdefghijklmnopqrstuvwxzABCDEFGHIJKLMNOPQRSTUVWXZY']
#split into individual letters
#letters = list(string[0])
#print(letters)

#num = ['0123456789']
#numbers = list(num[0])
#print(numbers)

#sym = ['!#$%&()*+']
#symbols = list(sym[0])
#print(symbols)

#Password Generator - password in sequence

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Z', 'Y']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the Password Generator")
pg_letters = int(input("How many letters would you like in your password?\n"))
pg_numbers = int(input("How many numbers would you like in your passwprd?\n"))
pg_symbols = int(input("How many numbers would you like in your password?\n"))

password = ""

for char in range(1, pg_letters + 1):
    password += random.choice(letters)

for char in range(1, pg_numbers + 1):
    password += random.choice(numbers)

for char in range(1, pg_symbols + 1):
    password += random.choice(symbols)

print(password)

# #Password Generator - PASSWORD IS JUMBLED

password_list = []

#we can rewrite the range as range starting from 0 instead of 1 to remove +1 at the end
for char in range(0, pg_letters):
    # append is similar to addition +=
    password_list.append(random.choice(letters))

for char in range(0, pg_numbers):
    password_list.append(random.choice(numbers))

for char in range(0, pg_symbols):
    password_list.append(random.choice(symbols))

#password output is list of charcaters
print(password_list)

#shuffle the character to generate different password each time
random.shuffle(password_list)
print(password_list)

#convert the list into string
gene_pass = ""
for char in password_list:
    gene_pass += char

print(f"Your password is {gene_pass}")