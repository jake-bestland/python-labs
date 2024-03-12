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

def battle(weapon_range: dict[str, range], opponent: int) -> str:
    for dmg in weapon_range.values():
        damage = random.choice(dmg)
    
    if damage >= opponent:
        return f"You win!" #Victory = True?
    else:
        return f"You Lost!" #Defeat = True? clear inventory?

chk_inv = {"check inventory", "check inv", "inv", "inventory", "i", "check i"}
chk_wpn = {"check weapon", "check w", "weapon", "w"}
pos_inp = {"yes", "keep going", "go on", "continue", "take", "take it", "follow", "ok", "okay", "sure", "fight", "y", "look", "look around", "use key", "key"}
neg_inp = {"no", "go back", "return", "nope", "leave it", "leave", "run away", "run", "head back", "back", "lobby", "n"}
take_leav_inp = f"take it or leave it?:\n"
dead_end = f"You head back to the lobby to continue on your adventure.\n"
win = "congratulations!! You won the game!"
lose = "Oh no!! the dragon was too powerful and ate you!  Game Over."
hands = {"hands": range(1, 2)}
sword = {"sword": range(4, 10)}
val_sword = {"valyrian steel sword": range(9, 13)}
key = "rusty key"
no_key = "no key"
bat_token = False
hero = False
l_path = False
armory = False
cur_weapon = {}
inventory = []  ### maybe add weapon inventory(dict) / item inventory.
cur_weapon.update(hands)
dragon = 10
evil_knight = 5


name = input("What is your name?: ")
print(f"Hello {name.capitalize()}, welcome to the game world!\nYou must defeat the dragon to win the game! The dragon is strong, so try and find a weapon to defeat it!\nYou can check your inventory or current weapon by entering 'i' or 'w' at any time.\n")
while hero == False:
    if bat_token == True:
        bat_token = False
    print("You're in the lobby and you see three doors.")
    path = input(f"Which door will you choose? The left, the middle, or the right?:\n").lower()
    if path in chk_inv:
        print(inventory)
    if path in chk_wpn:
        print(cur_weapon)
    if path == "left" or path == "the left":
        if l_path == True:
            print(f"You have already checked behind this door. Please choose a different door.\n")
        print("You have entered a seemingly empty room.")
        while l_path == False:
            l_option = input(f"Do you want to look around, or head back to the lobby?\n").lower()
            if l_option in chk_inv:
                print(inventory)
            if l_option in chk_wpn:
                print(cur_weapon)
            if l_option in neg_inp:
                continue
            elif l_option in pos_inp:
                print("You found a sword!")
                while True:
                    take = input(take_leav_inp).lower()
                    if take in chk_inv:
                        print(inventory)
                    if take in chk_wpn:
                        print(cur_weapon)
                    if take in pos_inp:
                        print("You now have a weapon to protect yourself!")
                        print(dead_end)
                        cur_weapon.clear()
                        cur_weapon.update(sword)
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
            r_option = input(f"Do you want to fight the dragon, or run away!?\n").lower()
            if r_option in chk_inv:
                print(inventory)
            if r_option in chk_wpn:
                print(cur_weapon)
            if r_option in neg_inp:
                continue
            elif r_option in pos_inp:
                if battle(cur_weapon, dragon) == "You win!":
                    print(f"You defeated the Dragon!\n")
                    hero = True
                    break
                if battle(cur_weapon, dragon) == "You Lost!":
                    inventory.clear()
                    cur_weapon.clear()
                    cur_weapon.update(hands)
                    print(lose)
                    break
            else:
                print("please choose, fight or run.")
                continue
    
    
    elif path == "middle" or path == "the middle" or path == "mid":
        print("You enter a dining room, and at the far end of the room, you see footprints leading down a dark hallway.")
        m_option = input(f"Do you want to head back to the lobby, or keep going?:\n").lower()
        if m_option in chk_inv:
            print(inventory)
        if m_option in chk_wpn:
            print(cur_weapon)
        if m_option in neg_inp:
            continue
        elif m_option in pos_inp:
            while bat_token == False:
                if key not in inventory and no_key not in inventory:
                    print("As you enter the room, you notice that there is a small rusty key on the table")
                    key_opt = input(take_leav_inp).lower()
                    if key_opt in chk_inv:
                        print(inventory)
                    if key_opt in chk_wpn:
                        print(cur_weapon)
                    if key_opt in pos_inp:
                        inventory.append(key)  ##add note to inventory file
                        print("You now have a rusty key.")
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
                        fight_knight = input(f"Fight the knight or run away!?\n").lower()
                        if fight_knight in chk_inv:
                            print(inventory)
                        if fight_knight in chk_wpn:
                            print(cur_weapon)
                        if fight_knight in neg_inp:
                            print("You try to run away, but he's too quick! You have no choice but to fight.")
                            if battle(cur_weapon, evil_knight) == "You win!":
                                print(f"You defeated the evil knight! Head back to the lobby to continue your adventure!\n")  ##add armor/shield? new weaopn?
                                bat_token = True
                                break
                            if battle(cur_weapon, evil_knight) == "You Lost!":
                                print(f"You were defeated by the evil knight!\n")
                                inventory.clear()
                                cur_weapon.clear()
                                cur_weapon.update(hands)
                                bat_token = True
                                break
                        if fight_knight in pos_inp:
                            if battle(cur_weapon, evil_knight) == "You win!":
                                print(f"You defeated the evil knight! Head back to the lobby to continue your adventure!\n")  ##add armor/shield? new weaopn?
                                bat_token = True
                                break
                            if battle(cur_weapon, evil_knight) == "You Lost!":
                                print(f"You were defeated by the evil knight!\n")
                                inventory.clear()
                                cur_weapon.clear()
                                cur_weapon.update(hands)
                                bat_token = True
                                break
                        else:
                            print("Please choose, fight or run.")
                            continue
                elif key in inventory:
                    print("You continue on and start to follow the footprints down the dark hallway.")
                    while armory == False:
                        lock_door_inp = input(f"You come across a locked door. Do you want to try the rusty key to see if it will open it? Or go back to the hallway?\n").lower()
                        if lock_door_inp in chk_inv:
                            print(inventory)
                        if lock_door_inp in chk_wpn:
                            print(cur_weapon)
                        if lock_door_inp in neg_inp:
                            inventory.append(no_key)
                            break
                        elif lock_door_inp in pos_inp:
                            print("You have come across an old armory!  It is mostly empty, but there is a valyrian steel sword hanging on the wall! ")
                            while True:
                                armory_inp = input(f"Do you want to take this weapon?\n").lower()
                                if armory_inp in chk_inv:
                                    print(inventory)
                                if armory_inp in chk_wpn:
                                    print(cur_weapon)
                                if armory_inp in neg_inp:
                                    print("This sword is too heavy anyway.")
                                    inventory.append(no_key)
                                    break
                                elif armory_inp in pos_inp:
                                    print("You now have a valyrian steel sword in your inventory.")
                                    cur_weapon.clear()
                                    cur_weapon.update(val_sword)
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
print(win)