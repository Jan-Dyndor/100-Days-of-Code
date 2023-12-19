#
# try:
#     file = open("file_name")
#     dictionary = {"key": "value"}
#     print(dictionary["NO_SUCH_KEY"])
# except FileNotFoundError:
#     file = open("file_name", "w")
#     file.write("")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     # All in try block was correctly executed
#     # But if there was ANY exception - else will not run
#     content = file.read()
#     print(content)
# finally:
#     # it runs no matter what happens
#     raise TypeError("Made up error")
#     # file.close()
#     # print("File was closed")
#

# Example
height = float(input("Weight: "))
weight = int(input("Height: "))
if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight/(height*height)
print(bmi)