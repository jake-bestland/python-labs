# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.

number = int(input("enter a number between 1 and 1,000,000,000: "))
if number >= 1 and number <= 1000000000:
    if number % 3 == 0:
        print("this number is divisible by 3")
    else:
        print("this number is not divisible by 3 evenly")
else:
    print("I'm sorry, this number is outside the range, please try again.")