# Take in a number between 1 and 12 from the user
# and print the name of the associated month:
# "January", "February", ... "December"
# Print "Error" if the number from the user is not between 1 and 12.
# Use a nested `if` statement.


number = int(input("please enter a number between 1 and 12.: "))

if number >= 1 and number <=12:
    if number == 1:
        print("January")
    if number == 2:
        print("February")
    if number == 3:
        print("March")
    if number == 4:
        print("April")
    if number == 5:
        print("May")
    if number == 6:
        print("June")
    if number == 7:
        print("July")
    if number == 8:
        print("August")
    if number == 9:
        print("September")
    if number == 10:
        print("October")
    if number == 11:
        print("November")
    if number == 12:
        print("December")
else:
    print("Error.")