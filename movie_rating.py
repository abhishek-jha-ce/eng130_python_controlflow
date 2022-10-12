# Program to check for what movies a user can watch

user_prompt = True

while user_prompt:
    user_age = input("Please enter your age: ")  # Ask User for their age
    if user_age.isdigit():  # Checks if the user has input numbers only
        if int(user_age) < 117:  # Checks if the user is less than 117 years old
            user_prompt = False
        else:
            print("You must be less than 117 Years Old!")
    else:
        print("Please enter a valid number")

# Assigning the movies category the user can watch.
age = int(user_age)

if age > 18: # If adult, you can watch any movies.
    print("You are " + user_age + " year Old. You can watch any movies you like")
elif age > 15: # If Older than 15
    print("You are " + user_age + " year Old. You can only watch \"U\" , \"PG\", \"12\" and, \"15\" rated movies")
elif age > 12:
    print("You are " + user_age + " year Old. You can only watch \"U\" , \"PG\" and, \"12\" rated movies")
elif age > 8:
    print("You are " + user_age + " year Old. You can only watch \"U\" and \"PG\" rated movies")
else:
    print("You are " + user_age + " year Old. You can only watch \"U\" rated movies")

# Another way of doing it
# if age < 8:  # If user is less than 8 Years Old, s/he can only watch U rated movies.
#     print("You are " + user_age + " year Old. You can only watch \"U\" rated movies")
# elif age < 12: # If less than 12 only U and PG
#     print("You are " + user_age + " year Old. You can only watch \"U\" and \"PG\" rated movies")
# elif age < 15: # If less than 15
#     print("You are " + user_age + " year Old. You can only watch \"U\" , \"PG\" and, \"12\" rated movies")
# elif age < 18: # If less than 18
#     print("You are " + user_age + " year Old. You can only watch \"U\" , \"PG\", \"12\" and, \"15\" rated movies")
# else:
#     print("You are " + user_age + " year Old. You can watch any movies you like")


