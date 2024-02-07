##Cesar Cypher

lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
#####new key codes= "hijklmnopqrstuvwxyzabcdefg"
secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7

secret = secret.lower()

new_key = lowercase_letters[cipher:] + lowercase_letters[0:cipher]
letter_index = ""
solution = ""

for char in secret:
    if char in lowercase_letters:
        letter_index = lowercase_letters.find(char)
        solution += new_key[letter_index]
    else:
        solution += char

solution = solution.capitalize()
print(solution)


    


#solution += new_key[letter_index]
    


#for char in secret:
#    if char.index(lowercase_letters[:]):