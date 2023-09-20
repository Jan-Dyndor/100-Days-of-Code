import random

from art import logo, vs
from game_data import data
from replit import clear


def format_data(account):
    """Takes the account data and returns the pritable fromat"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr} from {account_country}"


def check_answer(guess, A_followers, B_followers):
    """Takes the user guess and fallowers counts and returns if they got it right"""
    if A_followers > B_followers:
        return guess == "a"
    else:
        return guess == "b"


score = 0
# Display art
print(logo)
game_should_conitue = True
account_B = random.choice(data)
while game_should_conitue:
    # Making accounts at position B become the next account on posiotion A

    # generate random accounts
    account_A = account_B
    account_B = random.choice(data)
    # Prevent to compare the same accounts
    while account_A == account_B:
        account_B = random.choice(data)

    # Format account data into a printable format

    print(f"Comapre A: {format_data(account_A)}")

    print(vs)
    print(f"Against B: {format_data(account_B)}")

    # Ask user for a guess
    guess = input("Who has more follwoers A or B?: ").lower()

    # Check if user is correct
    #  get follower count of each account
    #  Use if statement to check if user is correct
    A_follow_account = account_A["follower_count"]
    B_follow_account = account_B["follower_count"]
    is_correct = check_answer(guess, A_follow_account, B_follow_account)
    # Clear the screen
    clear()
    # Display art
    print(logo)
    # Give user a feedback on their guess
    if is_correct:
        score += 1
        print(f"You are right! Current score is {score}")
    else:
        print(f"Sorry thats wrong. Finale score is {score}")
        game_should_conitue = False
    # Make a game reapeatable
