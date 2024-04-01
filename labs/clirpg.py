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
import requests

def battle(weapon_range: dict[str, range], opponent: int) -> str:
    for dmg in weapon_range.values():
        damage = random.choice(dmg)
    
    if damage >= opponent:
        return f"You win!"
    else:
        return f"You Lost!"

chk_inv = {"check inventory", "check inv", "inv", "inventory", "i", "check i"}
chk_wpn = {"check weapon", "check w", "weapon", "w"}
pos_inp = {"yes", "keep going", "go on", "continue", "take", "take it", "follow", "ok", "okay", "sure", "fight", "y", "look", "look around", "use key", "key"}
neg_inp = {"no", "go back", "return", "nope", "leave it", "leave", "run away", "run", "head back", "back", "lobby", "n"}
take_leav_inp = f"take it or leave it?:\n"
dead_end = f"You head back to the lobby to continue on your adventure.\n"
win = "congratulations!! You won the game!"
lose = "Oh no!! the dragon was too powerful and ate you!  Game Over."
hands = {"hands": range(1, 2)}
sword = {"dull sword": range(4, 10)}
val_sword = {"valyrian steel sword": range(9, 13)}
key = "rusty key"
game_over = False
hero = False
l_path = False
cur_weapon = {}
inventory = []
cur_weapon.update(hands)
dragon = 10
evil_knight = 5
min_name_len = 3
max_name_len = 6
url = f"https://uzby.com/api.php?min={min_name_len}&max={max_name_len}"
drag_name = requests.get(url).text
ev_kngt_name = requests.get(url).text

name = input("What is your name?: ")
print(f"Hello {name.capitalize()}, welcome to the game world!\nYou must defeat the dragon to win the game! The dragon is strong, so try to find a weapon to defeat it!\nYou can check your inventory or current weapon by entering 'i' or 'w' at any time.\n")
while game_over == False:
    print("You're in the lobby and you see three doors.")
    path = input(f"Which door will you choose? The left, the middle, or the right?:\n").lower()
    if path in chk_inv:
        print(inventory)
    if path in chk_wpn:
        print(cur_weapon)
    if path == "left" or path == "the left":
        if cur_weapon == sword:
            print(f"You have already checked behind this door. Please choose a different door.\n")
            continue
        print("You have entered a seemingly empty room.")
        while l_path == False:
            l_option = input(f"Do you want to look around, or head back to the lobby?\n").lower()
            if l_option in chk_inv:
                print(inventory)
            if l_option in chk_wpn:
                print(cur_weapon)
            if l_option in neg_inp:
                break
            elif l_option in pos_inp:
                print("You found a dull sword!")
                while True:
                    if cur_weapon == val_sword:
                        print("You currently have a more powerful weaopn. Would you like to replace your current weapon anyway?")
                    take = input(take_leav_inp).lower()
                    if take in chk_inv:
                        print(inventory)
                    if take in chk_wpn:
                        print(cur_weapon)
                    if take in pos_inp:
                        print("You now have a dull sword to protect yourself!")
                        print(dead_end)
                        cur_weapon.clear()
                        cur_weapon.update(sword)
                        l_path = True
                        break
                    elif take in neg_inp:
                        print("You decide that you don't need this sword.")
                        print(dead_end)
                        if cur_weapon == val_sword:
                            l_path = True
                        break
                    else:
                        print("Please choose, take it or leave it.")
                        continue
            else:
                print("Please choose, 'yes' to look around or 'no' to head back.")
                continue   
    
    elif path == "right" or path == "the right":
        print(f"You've encountered {drag_name} the dragon!")
        while True:
            r_option = input(f"Do you want to fight {drag_name}, or run away!?\n").lower()
            if r_option in chk_inv:
                print(inventory)
            if r_option in chk_wpn:
                print(cur_weapon)
            if r_option in neg_inp:
                print(f"You were able to safely escape {drag_name} and made your way back to the lobby!")
                break
            elif r_option in pos_inp:
                if battle(cur_weapon, dragon) == "You win!":
                    print(f"You defeated {drag_name}, the Dragon!\n")
                    game_over = True
                    hero = True
                    break
                if battle(cur_weapon, dragon) == "You Lost!":
                    inventory.clear()
                    cur_weapon.clear()
                    cur_weapon.update(hands)
                    print(f"{drag_name} was too powerful and defeated you! You manage to escape, but you lost everything you had!")
                    break
            else:
                print("please choose, fight or run.")
                continue
    
    elif path == "middle" or path == "the middle" or path == "mid":
        if cur_weapon == val_sword:
            print(f"You have already checked behind this door. Please choose a different door.\n")
            continue
        bat_token = False
        no_key = False
        armory = False
        unlock = False
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
                if key not in inventory and no_key == False:
                    print("As you enter the room, you notice that there is a small rusty key on the table")
                    key_opt = input(take_leav_inp).lower()
                    if key_opt in chk_inv:
                        print(inventory)
                    if key_opt in chk_wpn:
                        print(cur_weapon)
                    if key_opt in pos_inp:
                        inventory.append(key)
                        print("You now have a rusty key.")
                        continue
                    elif key_opt in neg_inp:
                        print("It's probably nothing.")
                        no_key = True
                        continue
                    else:
                        print("Please choose, take it or leave it.")
                elif key in inventory or no_key == True:
                    print(f"You continue down the dark hallway and come across {ev_kngt_name}, the evil knight, guarding a door!!")
                    while armory == False:
                        fight_knight = input(f"Fight {ev_kngt_name} or run away!?\n").lower()
                        if fight_knight in chk_inv:
                            print(inventory)
                        if fight_knight in chk_wpn:
                            print(cur_weapon)
                        if fight_knight in neg_inp:
                            print(f"You try to run away, but {ev_kngt_name}'s too quick! You have no choice but to fight.")
                            if battle(cur_weapon, evil_knight) == "You win!":
                                print(f"You defeated {ev_kngt_name}! You go over and check the door that he was guarding.\n")
                                bat_token = True
                                while unlock == False:
                                    lock_door_inp = input(f"The door {ev_kngt_name} was guarding is locked. Do you want to try the rusty key to see if it will open it? Or go back to the lobby?\n").lower()
                                    if lock_door_inp in chk_inv:
                                        print(inventory)
                                    if lock_door_inp in chk_wpn:
                                        print(cur_weapon)
                                    if lock_door_inp in neg_inp:
                                        armory = True
                                        break
                                    elif lock_door_inp in pos_inp:
                                        if key not in inventory:
                                            print("You do not have a key to unlock the door. Head back and try to find the key.")
                                            armory = True
                                            break
                                        if key in inventory:
                                            print("You have come across an old armory!  It is mostly empty, but there is a valyrian steel sword hanging on the wall! ")
                                            while True:
                                                armory_inp = input(f"Do you want to take this weapon?\n").lower()
                                                if armory_inp in chk_inv:
                                                    print(inventory)
                                                if armory_inp in chk_wpn:
                                                    print(cur_weapon)
                                                if armory_inp in neg_inp:
                                                    print(f"This sword is too heavy anyway. Head back to the lobby to continue your adventure!\n")
                                                    unlock = True
                                                    armory = True
                                                    break
                                                elif armory_inp in pos_inp:
                                                    print(f"You now have a valyrian steel sword in your inventory. Head back to the lobby to continue your adventure!\n")
                                                    cur_weapon.clear()
                                                    cur_weapon.update(val_sword)
                                                    unlock = True
                                                    armory = True
                                                    break
                                                else:
                                                    print("Please choose, yes or no.")
                                                    continue
                                    else:
                                        print("Please choose, yes or no.")
                                        continue
                            if battle(cur_weapon, evil_knight) == "You Lost!":
                                print(f"You were defeated by {ev_kngt_name}! He took everything you had! head back to the lobby.\n")
                                inventory.clear()
                                cur_weapon.clear()
                                cur_weapon.update(hands)
                                bat_token = True
                                break
                        if fight_knight in pos_inp:
                            if battle(cur_weapon, evil_knight) == "You win!":
                                print(f"You defeated {ev_kngt_name}! You go over and check the door that he was guarding.\n")
                                bat_token = True
                                while unlock == False:
                                    lock_door_inp = input(f"The door {ev_kngt_name} was guarding is locked. Do you want to try the rusty key to see if it will open it? Or go back to the lobby?\n").lower()
                                    if lock_door_inp in chk_inv:
                                        print(inventory)
                                    if lock_door_inp in chk_wpn:
                                        print(cur_weapon)
                                    if lock_door_inp in neg_inp:
                                        armory = True
                                        break
                                    elif lock_door_inp in pos_inp:
                                        if key not in inventory:
                                            print("You do not have a key to unlock the door. Head back and try to find the key.")
                                            armory = True
                                            break
                                        if key in inventory:
                                            print("You have come across an old armory!  It is mostly empty, but there is a valyrian steel sword hanging on the wall! ")
                                            while True:
                                                armory_inp = input(f"Do you want to take this weapon?\n").lower()
                                                if armory_inp in chk_inv:
                                                    print(inventory)
                                                if armory_inp in chk_wpn:
                                                    print(cur_weapon)
                                                if armory_inp in neg_inp:
                                                    print(f"This sword is too heavy anyway. Head back to the lobby to continue your adventure!\n")
                                                    unlock = True
                                                    armory = True
                                                    break
                                                elif armory_inp in pos_inp:
                                                    print(f"You now have a valyrian steel sword in your inventory. Head back to the lobby to continue your adventure!\n")
                                                    cur_weapon.clear()
                                                    cur_weapon.update(val_sword)
                                                    unlock = True
                                                    armory = True
                                                    break
                                                else:
                                                    print("Please choose, yes or no.")
                                                    continue
                                    else:
                                        print("Please choose, yes or no.")
                                        continue
                            if battle(cur_weapon, evil_knight) == "You Lost!":
                                print(f"You were defeated by {ev_kngt_name}! He took everything you had! head back to the lobby.\n")
                                inventory.clear()
                                cur_weapon.clear()
                                cur_weapon.update(hands)
                                bat_token = True
                                break
                        else:
                            print("Please choose, fight or run.")
                            continue
        else:
            print("please choose, return or keep going.")
            continue
    else:
        print("please choose left, middle or right")
        continue
if hero == True:
    print(win)