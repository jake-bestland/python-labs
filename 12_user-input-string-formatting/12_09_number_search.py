# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.


number = int(input("Please enter a number between 1 and 1,000,000,000.: "))

count = 0
while count != number:
    count += 1
print(count)

