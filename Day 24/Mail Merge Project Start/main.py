
names = list()
with open("Input/Names/invited_names.txt", mode="r") as names_file:
    for name in names_file:
        names.append(name.strip())


with open("Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter = letter_file.readlines()

letter_to_as_string = "".join(letter)

for name in names:
    with open(f"./Output/ReadyToSend/Letter_{name}", mode="w") as invitation:
        named_invitation = letter_to_as_string.replace("[name]", name)
        invitation.write(named_invitation)
