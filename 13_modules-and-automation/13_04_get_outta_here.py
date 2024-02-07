# Use the built-in `sys` module to explicitly quit your script.
# Include this functionality into a loop where you're asking the user
# for input in an infinite `while` loop.
# If the user enters the word "quit", you can exit the program
# using a functionality provided by this module.
import sys

word = "hello"
guess = None
while guess != word:
    guess = input("Guess the word: ")
    guess = guess.lower()
    if guess == word:
        print("congratulations! You won!")
        break
    elif guess == "quit":
        sys.exit()
    else:
        print(f"nope. sorry, guess again.")

