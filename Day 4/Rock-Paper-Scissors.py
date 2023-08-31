rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Write your code below this line 👇

choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n")
)

if choice not in range(0, 3):
    print("Invalid number, You lose")
    quit()

shapes_list = [rock, paper, scissors]
print(shapes_list[choice])

import random

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(shapes_list[computer_choice])

if choice == computer_choice:
    print("DRAW!")
elif choice == 0 and computer_choice == 2:
    print("You won!")
elif choice == 2 and computer_choice == 1:
    print("You won!")
elif choice == 1 and computer_choice == 0:
    print("You won!")
else:
    print("You lose")
