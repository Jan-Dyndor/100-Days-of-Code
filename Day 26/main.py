import random

# List Comprehension
# new_list = [new_item for item in old_list]

# numbers = [1,2,3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)
# print(new_list)
#
# new_list_comp = [n+1 for n in numbers]
# print(new_list_comp)
#
#
# name = "Jan"
# new_list = [letter for letter in name]
# print(new_list)


# new_list = [number * 2 for number in range(1,5)]
# print(new_list)



# # Conditional List Comprehension
# # new_list = [new_item for item in list if test]
# names = ["Alex", "Beth", "Caroline", "Dave", "Elenor", "Freddie"]
# short_names = [name for name in names if len(name) <= 4]
# print(short_names)
#
# long_names_upper = [name.upper() for name in names if len(name) > 5]
# print(long_names_upper)



# Dictionary Comprehension
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}

names = ["Alex", "Beth", "Caroline", "Dave", "Elenor", "Freddie"]
student_scores = {name: random.randint(0, 100) for name in names}
print(student_scores)
