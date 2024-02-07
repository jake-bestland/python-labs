# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings


word_1 = input("please type any word: ")
word_2 = input("choose a different word: ")
word_3 = input("enter another word, different than the other two: ")


if len(word_1) > len(word_2) and len(word_1) >len(word_3):
    print(f"{len(word_1)}, {word_1} ")
elif len(word_2) > len(word_1) and len(word_2) > len(word_3):
    print(f"{len(word_2)}, {word_2}")
elif len(word_3) > len(word_1) and len(word_3) > len(word_2):
    print(f"{len(word_3)}, {word_3}")
else:
    print("There is a tie for the longest word")