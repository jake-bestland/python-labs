# Write a Hangman game in Python.
# Users should have a limited amount of attempts to guess a pre-defined word.
# Print feedback to the user when they made a guess,
# and keep track of and communicate their remaining attempts.

# Hard-code a word that needs to be guessed in the script

# Print an explanation to the user

# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"

# Ask for user input

# Allow only single-character alphabetic input

# Create a counter for how many tries a user has

# Keep asking them for their guess until they won or lost

# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"

# Display a winning message and the full word if they win

# Display a losing message and quit the game if they don't make it


count = 8
word = "hangman"
word = word.lower()
correct_guess = ""
guess = None
final = True

name = input("What is your name?: ")
print(f"Welcome to my game of hangman, {name}! Try to guess what the secret word is.  You can only guess incorrectly {count} times!")

print("The secret word is:")
len_word = len(word)
print(word.replace(word, "_ " * len_word))

while True:
    if count == 0:
        print("You are out of guesses. Game over!")
        break
    guess = input("Guess a letter: ")
    guess = guess.lower()
    if len(guess) != 1:
        print("please only guess one letter") 
        continue
    
    if guess in correct_guess:
        print("You have already guessed this letter!")
        continue

    if guess in word:
    #    amount = word.count(guess)
    #    correct_guess += guess * amount
        correct_guess += guess
    else:
        count -= 1
        print(f"nope, sorry! that is not one of the letters guess again.  You have {count} tries remaining.")
    final = True
    for char in word:
        if char in correct_guess:
            print(char, end= " ")
        else:
            final = False
            print("_", end= " ")

    
    if final:
        print("Congratulations! You guessed the word before you ran out of tries! You Win!")
        break
