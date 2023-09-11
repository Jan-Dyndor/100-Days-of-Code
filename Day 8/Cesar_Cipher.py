import art

# from replit import clear
import os

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char == " " or char == char.isdigit() or not char.isalpha():
            end_text += char
            continue
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]

    print(f"Here's the {cipher_direction}d result: {end_text}")


play = "yes"
while play == "yes":
    print(art.logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # if the user enters a shift that is greater than the number of letters in the alphabet
    new_shift = shift
    if shift > 26:
        new_shift = shift % 26
    caesar(start_text=text, shift_amount=new_shift, cipher_direction=direction)
    play = input("Do you want to play agian yes/no? ")
    # clear()
    os.system("cls")
print("Thanks for using! Keep your secrets private!")
