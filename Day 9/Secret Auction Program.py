# from replit import clear
import os

import art

players_dict = {}
print(art.logo)
print("Welcome to the secret auction program!")
more_players = True
while more_players:
    player_name = input("What is your name?: ")
    player_bid = float(input("What is your bid?: $"))
    players_dict[player_name] = player_bid
    other_players = input("Are there any other players? Type 'yes' or 'no': \n")
    if other_players == "no":
        more_players = False
    # clear()
    os.system("cls")

max_value = None
winner = ""
for key, value in players_dict.items():
    if max_value is None or value > max_value:
        max_value = value
        winner = key


print(f"The winner is {winner} with a bid of {max_value}$")
