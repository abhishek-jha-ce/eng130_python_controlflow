data = 0

# while data < 10:
#     print(f"It's working - > {data}")
#     if data == 5:
#         # break # Keyword to break from loop
#         continue #
#     data += 1

user_prompt = True
current_year = 2022

while user_prompt:
    age = input("Please Enter your Age: ")
    if age.isdigit():
        user_prompt = False
    else:
        print("Please enter your age in digits only")

born_year = current_year - int(age)
print(f"You were born in {born_year}")  # Output: Displays the year user was born
