# Day 26 - Intermediate - List Comprehension and the NATO Alphabet

Important! A `list` in a shorthand  is any kind of iterable like List, string, range, tuple

What I have learned:
## List Comprehension
new_list = [new_item for item in list]

Conditional List Comprehension
new_list = [new_item for item in list if test]
Adds the new and preform the new_item code only if test passes (is true)

## Dictionary Comprehension 
new_dict = {new_key:new_value for item in list}
Thins is just a way to create a Dictionary using shorter syntax 

Creating a dictionary based on a values in existing dictionary
new_dict = {new_key:new_value for (key,value) in dict.items() }

Conditional dictionary comprehension 
new_dict = {new_key:bew_value for (key, value) in dict.items() if test}

