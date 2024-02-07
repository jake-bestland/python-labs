# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.

name = input("What is your name?: ")
firstname = ""
for letter in name:
    if letter != " ":
        firstname += letter
    if letter == " ":
        break

print(f"Hello {firstname}! Welcome to my script!")
