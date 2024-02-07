# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.


user_str = input("write a sentece here: ")
user_str = user_str.lower()

a = 0
e = 0
i = 0
o = 0
u = 0

for char in user_str:
    if char == "a":
        a += 1
    if char == "e":
        e += 1
    if char == "i":
        i += 1
    if char == "o":
        o += 1
    if char == "u":
        u += 1

print(f"There are {a} 'A' vowles, {e} 'E' vowles, {i} 'I' vowles, {o} 'O' vowles, and {u} 'U' vowles in your sentence.")