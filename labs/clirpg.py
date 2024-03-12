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
    damage = random.choice(weapon)
    if damage >= opponent:
        return f"You win!" #Victory = True?
    else:
        return f"You Lost!" #Defeat = True? clear inventory?


pos_inp = {"yes", "keep going", "go on", "continue", "take", "take it", "follow", "ok", "okay", "sure", "fight", "y", "look", "look around"}
neg_inp = {"no", "go back", "return", "nope", "leave it", "leave", "run away", "run", "head back", "back", "lobby", "n"}
take_leav_inp = "take it or leave it?: "
dead_end = "Head back to the lobby and go through another door."
win = "congratulations!! You slayed the dragon and won the game!"
lose = "Oh no!! the dragon was too powerful and ate you!  Game Over."
hands = range(1, 2)
sword = range(4, 10)
val_sword = range(9, 13)
key = "rusty key"
no_key = "no key"
vic_token = False
loss_token = False
hero = False
l_path = False
armory = False
inventory = []  ### maybe add weapon inventory(dict) / item inventory.
inventory.append(hands)
dragon = 10
evil_knight = 5


name = input("What is your name?: ")
print(f"Hello {name.capitalize()}, welcome to the game world!")
while hero == False:
    if loss_token == True:
        loss_token = False
    print("You're in the lobby and you see three doors.")
    path = input("Which door will you choose? The left, the middle, or the right?: ").lower()
    
    if path == "left" or path == "the left":
        print("You have entered a seemingly empty room.")
        while l_path == False:
            l_option = input("Do you want to look around, or head back to the lobby?").lower()
            if l_option in neg_inp:
                continue
            elif l_option in pos_inp:
                print("You found a sword!")
                while True:
                    take = input(take_leav_inp).lower()
                    if take in pos_inp:
                        print("You now have a weapon to protect yourself!")
                        print(dead_end)
                        inventory.remove(inventory[0])
                        inventory.insert(0, sword)   ### add write/append file for inventory update
                        l_path = True
                        break
                    elif take in neg_inp:
                        print("You don't need any weapons for protection!")
                        print(dead_end)
                        ####l_path = True???### not having l_path = True allows them to go back and get the sword.
                        break
                    else:
                        print("Please choose, take it or leave it.")
                        continue
            else:
                print("Please choose, 'yes' to look around or 'no' to head back.")
                continue   
    
    elif path == "right" or path == "the right":
        print("You've encountered a dragon!")
        while True:
            r_option = input("Do you want to fight the dragon, or run away!? ").lower()
            if r_option in neg_inp:
                continue
            elif r_option in pos_inp:
                if battle(inventory[0], dragon) == "You win!":
                    print(win)
                    hero == True
                    break
                if battle(inventory[0], dragon) == "You Lost!":
                    inventory.clear()
                    print(lose)
                    break
            else:
                print("please choose, fight or run.")
                continue
    
    
    elif path == "middle" or path == "the middle" or path == "mid":
        print("You enter a dining room, and at the far end of the room, you see footprints leading down a dark hallway.")
        m_option = input("Do you want to head back to the lobby, or keep going?: ").lower()
        if m_option in neg_inp:
            continue
        elif m_option in pos_inp:
            while loss_token == False or vic_token == False:
                if key not in inventory and no_key not in inventory:
                    print("As you enter the room, you notice that there is a small rusty key on the table")
                    key_opt = input(take_leav_inp).lower()
                    if key_opt in pos_inp:
                        inventory.append(key)  ##add note to inventory file
                        print("You now have a rusty key")
                        continue
                    elif key_opt in neg_inp:
                        print("It's probably nothing.")  ##add no_key to inventory?
                        inventory.append(no_key)  ##add note to inventory file
                        continue
                    else:
                        print("Please choose, take it or leave it.")
                elif no_key in inventory:
                    print("You continue down the hallway and it lead you to a dungeon, where you come across an evil knight!")
                    while True:
                        fight_knight = input("Fight the knight or run away!? ").lower()
                        if fight_knight in neg_inp:
                            print("You try to run away, but he's too quick! You have no choice but to fight.")
                            if battle(inventory[0], evil_knight) == "You win!":
                                print("You defeated the evil knight! Head back to the lobby to continue your adventure!")  ##add armor/shield? new weaopn?
                                vic_token = True
                                break
                            if battle(inventory[0], evil_knight) == "You Lost!":
                                print("You were defeated by the evil knight!")
                                inventory.clear()
                                inventory.append(hands)
                                loss_token = True
                                break
                        if fight_knight in pos_inp:
                            if battle(inventory[0], evil_knight) == "You win!":
                                print("You defeated the evil knight! Head back to the lobby to continue your adventure!")  ##add armor/shield? new weaopn?
                                vic_token = True
                                break
                            if battle(inventory[0], evil_knight) == "You Lost!":
                                print("You were defeated by the evil knight!")
                                inventory.clear()
                                inventory.append(hands)
                                loss_token = True
                                break
                        else:
                            print("Please choose, fight or run.")
                            continue
                elif key in inventory:
                    print("You follow the footprints down the dark hallway and come across a locked door.")
                    while armory == False:
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
                                    armory = True
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