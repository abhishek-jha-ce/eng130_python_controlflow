data = 0

# while data < 10:
#     print(f"It's working - > {data}")
#     if data == 5:
#         # break # Keyword to break from loop
#         continue #
#     data += 1

# age = 7;
user_prompt = True

while user_prompt:
    age = input("please enter your age")
    if age.isdigit():
        user_prompt = False
    else:
        print("Please enter your age in digits only")

print(f"Your age is {age}")
