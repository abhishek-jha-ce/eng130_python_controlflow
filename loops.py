# list_data = [1, 2, 3, 4, 5]
# for number in list_data:
#     if number == 3:
#         print("Found 3")
#     elif number > 3:
#         print("You have passed 3")
#     else:
#         print("too soon")

"""
create a dictionary
itreate through the dict
using control flow - if elif else and for loop print all the keys
print all the value
print key with matching values
"""

# Dictionary
student = {
    "first_name": "Abhishek",
    "last_name": "Jha",
    "Stream": "DevOps",
    "Location": "London",
    "Salary": 1000
}

# Keys in Dictionary
print("Printing the keys in Dict:")
print(student.keys())

print("Printing the values in Dict:")
print(student.values())

# Using Loops
print("Printing the keys in Dict:")
for key in student:
    print(key)

print("Printing the values in Dict:")
for value in student.values():
    print(value)


print("Printing Keys and Values using loop")
for key, value in student.items():
    print(key, ':', value)
