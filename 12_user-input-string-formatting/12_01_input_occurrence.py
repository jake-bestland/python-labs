# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4


while True:
    user_str = input("Say something.: ")
    user_let = input("now pick out a letter within the words you just entered.: ")
    if user_let in user_str:
            print("That letter first occurs at an index of " + str(user_str.find(user_let)))
            break
    else:
        print("please pick a letter you used.")
        continue