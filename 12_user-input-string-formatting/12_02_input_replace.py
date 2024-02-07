# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please


user_str = input("write a sentence.: ")
user_sym = input("enter a symbol.: ")


print(user_str.replace(user_str[0] , user_sym))