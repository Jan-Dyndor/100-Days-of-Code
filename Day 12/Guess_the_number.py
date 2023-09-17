import random

# from art import logo


def choose_number():
    """Function returns a random numbr 1-100"""
    return random.randint(1, 100)


def choose_level(level):
    """Function changes the number of attempts depending on difficulty leve player has choose"""
    # Next time i will try not to modify global variable because is not a best practice
    global attempts
    if level == "hard":
        attempts = 5


def compare_numbers(user_guessed_number, random_numumber):
    """Function compares a numbers and returns 0 if number was not guessed and 1 if guess was correct"""
    if user_guessed_number > random_number:
        print("Too high!")
        return 0
    elif user_guessed_number < random_number:
        print("Too low!")
        return 0
    else:
        return 1


attempts = 10

# print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
choose_level(level)
random_number = choose_number()
print(f"pssst we choose {random_number}")

while attempts > 0:
    print(f"You have {attempts} remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if compare_numbers(guess, random_number):
        print("You got it!")
        attempts = 0
    attempts -= 1
    if attempts == 0:
        print(f"You lost! The choosen number was {random_number}")
