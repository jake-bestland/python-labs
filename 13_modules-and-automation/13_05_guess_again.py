# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.
import random

num = random.randint(1, 10)
guess = None
count = 6
while guess != num:
    guess = input("Guess a number between 1 and 10: ")
    if guess == num:
        print("Congrats! You win!")
        break
    else:
        count -= 1
        print(f"Nope, sorry! Guess again! You have {count} guesses remaining.")
        if count == 0:
            print("You are out of guesses, you lose!")
            break
        