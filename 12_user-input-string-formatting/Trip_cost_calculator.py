#Trip cost calculator:

distance = input("How many kilometers will you drive?: ")
efficiency = input("How many liters-per-kilometer does you car use?: ")
price = input("What is the cost per liter of fuel?: ")
distance = int(distance)
efficiency = int(efficiency)
price = float(price)

print(f"Your trip will cost you ${(distance / efficiency) * price} ")