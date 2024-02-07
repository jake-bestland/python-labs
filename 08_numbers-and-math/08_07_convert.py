# Demonstrate how to:
# -------------------
# 1) Convert an int to a float
# 2) Convert a float to an int
# 3) Perform division using a float and an int.
# 4) Use two variables to perform a multiplication.
#
# What information is lost during which conversions?

#1
num = 40
float(num)
number = float(num)
print(type(number))

#2
num = 41.5
int(num)
number = int(num)
print(type(number))
print(number)

#3
print(8.5 / 10)

#4
height = 5
width = 8
print(height * width)

#when converting a float to an int, you lose the remainder or the numbers after the decimal point.