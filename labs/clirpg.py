# Build a CLI RPG game following the instructions from the course.

# Ask the player for their name.

# Display a message that greets them and introduces them to the game world.

# Present them with a choice between two doors.

# If they choose the left door, they'll see an empty room.

# If they choose the right door, then they encounter a dragon.
 
# In both cases, they have the option to return to the previous room or interact further.

# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.

# When encountering the dragon, they have the choice to fight it.

# If they have the sword from the other room, then they will be able to defeat it and win the game.

# If they don't have the sword, then they will be eaten by the dragon and lose the game.



path = "Which door will you choose? The left, or the right?: "
left_door = "You see an empty room."
right_door = "You've encountered a dragon!"
dead_end = "Head back to the begining and go through the other door."
win = "congratulations!! You slayed the dragon and won the game!"
lose = "Oh no!! the dragon was too powerful and ate you!  Game Over."
sword = False

name = input("What is your name?: ")
print(f"Hello {name}, welcome to the game world!")
while True:
    print("You see two doors.")
    choose = input(path)
    choose = choose.lower()
    if choose == "left":
        print(left_door)
        option = input("Do you want to return, or interact further?: ")
        option = option.lower()
        if option == "return":
            continue
        elif option == "interact" or option == "interact further":
            look = input("Do you wish to look around the seemingly empty room?: ")
            look = look.lower()
            if look == "no":
                print(dead_end)
                continue
            elif look == "yes":
                print("You found a sword!")
                take = input("take it or leave it?: ")
                take = take.lower()
                if take == "take it" or take == "yes":
                    print("You now have a weapon to protect yourself!")
                    print(dead_end)
                    sword = True
                    continue
                elif take == "leave it" or take == "no":
                    print("You don't need any weapons for protection!")
                    print(dead_end)
                else:
                    print("Please choose, take it or leave it.")
            else:
                print("Please choose, yes or no.")
        else:
            print("please choose, return or interact.")
    elif choose == "right":
        print(right_door)
        option = input("Do you want to return, or interact further?: ")
        option = option.lower()
        if option == "return":
            continue
        elif option == "interact" or option == "interact further":
            fight = input("Do you want to fight the dragon?: ")
            fight = fight.lower()
            if fight == "no":
                print(dead_end)
                continue
            elif fight == "yes":
                if sword == True:
                    print(win)
                    break
                elif sword == False:
                    print(lose)
                    break
            else:
                print("Please choose, yes or no.")
        else:
            print("please choose, return or interact.")
    else:
        print("please choose left or right")