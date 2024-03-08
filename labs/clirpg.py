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


# Save the user input options you allow, e.g., in a set that you can check against when your user makes a choice.
# Create an inventory for your player, where they can add and remove items.
# Players should be able to collect items they find in rooms and add them to their inventory.
# If they lose a fight against the dragon, then they should lose their inventory items.
# Add more rooms to your game and allow your player to explore.
# Some rooms can be empty, others can contain items, and yet others can contain an opponent.
# Implement some logic that decides whether or not your player can beat the opponent depending on what items they have in their inventory
# Use the random module to add a multiplier to your battles, similar to a dice roll in a real game. This pseudo-random element can have an effect on whether your player wins or loses when battling an opponent.

import random

def battle(weapon, opponent):
    if random.randint(weapon) >= opponent:
        return f"You win!" #Victory = True?
    else:
        return f"You Lost!" #Defeat = True? clear inventory?


pos_inp = {"yes", "keep going", "go on", "continue", "take", "take it", "follow", "ok", "okay", "sure", "fight"}
neg_inp = {"no", "go back", "return", "nope", "leave it", "leave", "run away", "run", "head back", "back", "lobby"}
path = "Which door will you choose? The left, the middle, or the right?: "
inp_opt = "Do you want to head back to the lobby, or keep going?: "
take_leav_inp = "take it or leave it?: "
dead_end = "Head back to the lobby and go through another door."
win = "congratulations!! You slayed the dragon and won the game!"
lose = "Oh no!! the dragon was too powerful and ate you!  Game Over."
hands = range(1, 2)
sword = range(4, 8)
val_sword = range(9, 13)
key = True
no_key = True
inventory = [] #inventory.clear() - if killed by dragon
inventory.append(hands)
dragon = 10
evil_knight = 5



# name = input("What is your name?: ")
# print(f"Hello {name.capitalize()}, welcome to the game world!")
while True:
    print("You're in the lobby and you see three doors.")
    choose = input(path).lower()
    if choose == "left":
        print("You have entered a seemingly empty room.")
        l_option = input(inp_opt).lower()
        if l_option in neg_inp:
            continue
        elif l_option in pos_inp:
            while True:
                look = input("Do you wish to look around the seemingly empty room?: ").lower()
                if look in neg_inp:
                    print(dead_end)
                    break
                    # continue
                elif look in pos_inp:
                    print("You found a sword!")
                    while True:
                        take = input(take_leav_inp).lower()
                        if take in pos_inp:
                            print("You now have a weapon to protect yourself!")
                            print(dead_end)
                            inventory.remove(inventory[0])
                            inventory.insert(0, sword)   ### add write/append file for inventory update
                            break
                        elif take in neg_inp:
                            print("You don't need any weapons for protection!")
                            print(dead_end)
                            break
                        else:
                            print("Please choose, take it or leave it.")
                            continue
                else:
                    print("Please choose, yes or no.")
                    continue
        else:
            print("please choose, return or keep going.")
            continue
    
    
    elif choose == "right":
        print("You've encountered a dragon!")
        r_option = input(inp_opt).lower()
        if r_option in neg_inp:
            continue
        elif r_option in pos_inp:
            while True:
                fight = input("Do you want to fight the dragon?: ").lower()
                if fight in neg_inp:
                    print(dead_end)
                    break
                elif fight in pos_inp:
                    if sword in inventory:
                        print(win)
                        break
                    elif sword not in inventory:
                        inventory.clear()
                        print(lose)
                        break
                else:
                    print("Please choose, yes or no.")
                    continue
        else:
            print("please choose, return or keep going.")
            continue
    
    
    elif choose == "middle" or choose == "the middle" or choose == "mid":
        print("You enter a dining room, and at the far end of the room, you see footprints leading down a dark hallway.")
        m_option = input(inp_opt).lower()
        if m_option in neg_inp:
            continue
        elif m_option in pos_inp:
            while True:
                if key not in inventory or no_key not in inventory: ##add no_key?
                    print("As you enter the room, you notice on the table there is a small rusty key")
                    key_opt = input(take_leav_inp).lower()
                    if key_opt in pos_inp:
                        inventory.append(key)  ##add note to inventory file
                        print("You now have a rusty key")
                        continue #
                    elif key_opt in neg_inp:
                        print("It's probably nothing.")  ##add no_key to inventory?
                        inventory.append(no_key)  ##add note to inventory file
                        continue
                    else:
                        print("Please choose, take it or leave it.")
                elif no_key in inventory:
                    print("You continue down the hallway and it lead you to a dungeon, where you come across an evil knight!")  ###########finish this path
                elif key in inventory:
                    print("You follow the footprints down the dark hallway and come across a locked door.")
                    while True:
                        lock_door_inp = input("Do you want to try the rusty key to see if it will open the door? Or go back to the hallway? ").lower()
                        if lock_door_inp in neg_inp:
                            inventory.append(no_key)
                            break
                        elif lock_door_inp in pos_inp:
                            print("You have come across an old armory!  It is mostly empty, but there is a valyrian steel sword hanging on the wall! ")
                            while True:
                                armory_inp = input("Do you want to take this weapon? ").lower()
                                if armory_inp in neg_inp:
                                    print("This sword is too heavy anyway.")
                                    inventory.append(no_key)
                                    break
                                elif armory_inp in pos_inp:
                                    print("You now have a valyrian steel sword in your inventory.")
                                    inventory.remove(inventory[0])
                                    inventory.insert(0, val_sword)
                                    inventory.append(no_key)
                                    break
                                else:
                                    print("Please choose, yes or no.")
                                    continue
                        else:
                            print("Please choose, yes or no.")
                            continue


        else:
            print("please choose, return or keep going.")
            continue
    else:
        print("please choose left, middle or right")
        continue