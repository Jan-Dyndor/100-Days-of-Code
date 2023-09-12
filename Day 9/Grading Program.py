student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}


# TODO-2: Write your code below to add the grades to student_grades.👇
for key, value in student_scores.items():
    # temporary vale not to change orginal dictionary
    temp_value = ""
    if value >= 91:
        temp_value = "Outstanding"
    elif value >= 81:
        temp_value = "Exceeds Expectations"
    elif value >= 71:
        temp_value = "Acceptable"
    else:
        temp_value = "Fail"
    student_grades[key] = temp_value


# 🚨 Don't change the code below 👇
print(student_grades)
print(student_scores)
