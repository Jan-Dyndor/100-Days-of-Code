# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
# #
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


import pandas as pd
# TODO 1. Create a dictionary in this format:  {"A": "Alfa", "B": "Bravo"}

nato_data = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}



#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# while True:
#     print(nato_dict)
#     word = input("Enter a word: ").upper()
#     try:
#         phonetic_words = [nato_dict[letter] for letter in word]
#         print(phonetic_words)
#         break
#     except KeyError:
#         print("Sorry, only letters in the alfabet please")
#         continue
#
#



def genarate_phonetics():
    word = input("Enter a world: ").upper()
    try:
        phonetic_words = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alfabet please")
        genarate_phonetics()
    else:
        print(phonetic_words)

genarate_phonetics()