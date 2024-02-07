# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.

user_input = input("What do you like most about coding? ")
result = ""
for char in range(len(user_input)):
    if not char % 2:
        result = result + user_input[char].upper()
    else:
        result = result + user_input[char].lower()

print(result)