##Cesar Cypher

lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
#####new key codes= "hijklmnopqrstuvwxyzabcdefg"
uppercaser_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7

low_key = lowercase_letters[cipher:] + lowercase_letters[0:cipher]
up_key = uppercaser_letters[cipher:] + uppercaser_letters[0:cipher]
letter_index = ""
solution = ""

for char in secret:
    if char in lowercase_letters:
        letter_index = lowercase_letters.find(char)
        solution += low_key[letter_index]
    elif char in uppercaser_letters:
        letter_index = uppercaser_letters.find(char)
        solution += up_key[letter_index]
    else:
        solution += char

print(solution)
