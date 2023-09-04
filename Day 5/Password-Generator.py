#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# password=""

# for random_letter in range(0,nr_letters):
#   letter_index = random.randint(0,len(letters)-1)
#   password += letters[letter_index]

# for random_symbol in range(0,nr_symbols):
#   symbol_index = random.randint(0,len(symbols)-1)
#   password += symbols[symbol_index]

# for random_number in range(0,nr_numbers):
#   number_index = random.randint(0,len(numbers)-1)
#   password += numbers[number_index]

# print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = list()

for random_letter in range(0, nr_letters):
    letter_index = random.randint(0, len(letters) - 1)
    password_list.append(letters[letter_index])

for random_symbol in range(0, nr_symbols):
    symbol_index = random.randint(0, len(symbols) - 1)
    password_list.append(symbols[symbol_index])

for random_number in range(0, nr_numbers):
    number_index = random.randint(0, len(numbers) - 1)
    password_list.append(numbers[number_index])

print(password_list)
print(len(password_list))

password2 = ""

for char in range(0, len(password_list)):
    random_index = random.randint(0, len(password_list) - 1)
    password2 += password_list.pop(random_index)

if not password_list:
    print("Checking if list is empty")
print(password2)

# I used 0 in range function not to add 1 every time to the second parameter, and second parameter is not included in range

# I could use a choice function instead of generating random number every time in for loop. For example:
#  for char in range(0,nr_letters)
#     password += random.choice(letters)

# I could also use a random.shuffle() on LIST instead of generating random number and poping item from list every time

# That exercise was amazing! I have learned so much!!!!!
