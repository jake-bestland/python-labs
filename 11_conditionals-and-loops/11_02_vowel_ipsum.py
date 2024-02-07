# Print the total number of vowels that are used in the lorem ipsum text.

lorem_ipsum = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut 
aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in 
voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt 
mollit anim id est laborum."""

#lorem_ipsum = lorem_ipsum.lower()
#solution = ""

#for char in lorem_ipsum:
#   if char in "aeiou":
#    solution += char

#print(len(solution))


lorem_ipsum = lorem_ipsum.lower()
solution = 0

for char in lorem_ipsum:
    if char in "aeiou":
        solution += 1
print(solution)