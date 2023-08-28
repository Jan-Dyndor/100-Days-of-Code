print(
    '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''
)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇
print(
    """ 
Once upon a time, in a dense, mysterious forest, there lived a brave adventurer named Alex. The forest was known for its enigmatic reputation and tales of hidden treasures that had lured countless explorers.

Alex had heard of these legends and was determined to uncover the secrets of the forest. One bright morning, with a trusty map in hand, Alex ventured into the depths of the woods, where sunlight struggled to penetrate the thick canopy of leaves.

As Alex journeyed deeper into the forest, the path diverged into two near small house. A signpost stood before him, weathered and ancient. 

"""
)

first_choice = input("It read, 'Choose your path: (Left) or (Right).'\n").lower()

if first_choice == "right":
    print(
        """The right path led to a dark cave filled with deadly spikes. With a sudden, terrifying fall, Alex met an untimely end. The forest's secrets remained hidden, forever untouched in the darkness.
  """
    )
    quit()
else:
    print(
        """ As Alex walked along the left path, he suddenly came across a vast, murky river blocking their way. On the other side, there seemed to be a hidden passage deeper into the forest. Alex contemplated their options and saw a boat tied to a nearby tree.
  """
    )
second_choice = input(
    """Should Alex (Swim) across the treacherous river, or should they (Wait) and examine the boat more closely?
"""
).lower()

if second_choice == "swim":
    print(
        """The current proved to be far stronger and more treacherous than it appeared. As Alex struggled against the raging waters, they were swiftly pulled into a powerful whirlpool that dragged them under.
  """
    )
    quit()
else:
    print(
        """Alex wisely chose to (Wait).

After some time, the sound of rustling leaves caught Alex's attention. Out of the dense underbrush emerged a wise old forest guardian. The guardian explained that swimming across the river would have led to a dangerous whirlpool that no one had ever survived. Alex's patience had saved him from a terrible fate.

The guardian then guided Alex to a clearing with three mysterious doors: one (Red), one (Blue), and one (Yellow). They explained that behind one of these doors lay the fabled treasure of the forest.

With a sense of anticipation, Alex considered their choices.
  """
    )
third_choice = input("Which door should they open?").lower()
if third_choice == "red":
    print(
        """ 
  Behind the red door, Alex encountered a room filled with riddles and enigmatic symbols. It seemed impossible to decipher and so Alex was trapped in endless riddle games
  """
    )
    quit()

elif third_choice == " blue":
    print(
        """ Upon opening the blue door, Alex found himself in a chamber filled with an intricate network of mirrors. The room was disorienting, with reflections creating an illusion of endless paths. He never menaged to escape that prison.
  """
    )
    quit()
elif third_choice == "yellow":
    print(
        """ Upon opening the yellow door, a brilliant, golden light filled the room. Before them lay a vast chamber filled with glittering jewels, precious metals, and the long-lost treasures of the forest. Alex had successfully unlocked the secret of the forest and found the legendary treasure!

The forest guardian smiled and congratulated Alex on their bravery and wisdom. Alex emerged from the forest, richer in both wealth and experience, knowing that they had made the right choices and unlocked the forest's greatest secret.

And so, the legend of the forest's hidden treasure lived on, with Alex's name forever etched into its history as the one who dared to make the right decisions and unearth the wealth that lay within the mysterious woods.
  """
    )
else:
    print(
        """Why did you choose non existing doors? Do you test the game? Were You looking for easter eggs?
  """
    )
    quit()
