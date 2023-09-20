# from replit import clear
import os
import random

import art
import game_data as gd


# Functions
def person_A(data_dict):
    """Random choice of person from dictionary. Print data and return data in  person variable"""
    person = random.choice(data_dict)
    print(
        "Compare A: "
        + person["name"]
        + " "
        + person["description"]
        + " "
        + person["country"]
    )
    return person


def person_B(data_dict):
    """Random choice of person from dictionary. Prints data and return person"""
    person = random.choice(data_dict)
    print(
        "Against B: "
        + person["name"]
        + " "
        + person["description"]
        + " "
        + person["country"]
    )
    return person


def who_has_more_followers(number_A, number_B):
    """Function compares a number of followers and returns A or B"""
    if number_A > number_B:
        return "A"
    else:
        return "B"


def choose(last_person, score):
    """Function will swap last B person and make it A person. With help of
    recursion will check if user guessed correctly if so the function will re-call itself if not will return current score
    """
    print(art.logo)
    print(f"Your score is {score}")
    print(
        "Compare A: "
        + last_person["name"]
        + " "
        + last_person["description"]
        + " "
        + last_person["country"]
    )
    A_number = last_person["follower_count"]
    print(art.vs)
    p_B = person_B(gd.data)
    B_number = p_B["follower_count"]
    if p_A == p_B:
        p_B = person_B(gd.data)
        B_number = p_B["follower_count"]
    # For testing purpose i will print A and B number of followers
    print(f"A = {A_number}, B = {B_number}")
    choice = input("Who has more followers? A or B: ").upper()
    if who_has_more_followers(A_number, B_number) == choice:
        score += 1
        # clear()
        os.system("cls")
        return choose(p_B, score)
    else:
        return score


score = 0
print(art.logo)
p_A = person_A(gd.data)
A_number = p_A["follower_count"]
print(art.vs)
p_B = person_B(gd.data)
B_number = p_B["follower_count"]
if p_A == p_B:
    p_B = person_B(gd.data)
    B_number = p_B["follower_count"]
# For testing purpose i will print A and B number of followers
print(f"A = {A_number}, B = {B_number}")
choice = input("Who has more followers? A czy B: ").upper()
if who_has_more_followers(A_number, B_number) == choice:
    # clear()
    os.system("cls")
    score += 1
    score = choose(p_B, score)

# clear()
os.system("cls")

print(f"Sorry, that's wrong. Final score: {score}")
