# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()


# Better way to opening a file !

# Read a file
with open("my_file.txt") as file:
    content = file.read()
    print(content)

# write to a file  mode="w" -- write remove files content and write
# If we want to leave the files content and just add something we use mode ="a"
# whitch means append
# with open("my_file.txt", mode="a") as file:
#     file.write("\nAnd I am a pharmacist and 3rd year CS student who want to make it to Machine Learning!")


with open("new_file.txt", mode="w") as file:
    file.write("new_file.txt does not exist in a current folder it will be created")
