# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

amount = input("What is the amount you have invested?: ")
rate = input("What percent is your interest rate?: ")
years = input("How many years do you wish to invest?: ")
amount = int(amount)
rate = int(rate)
years = int(years)

rate = rate / 100

value_per_year = amount * rate

if years > 1:
    print(f"After {years} years, your investment will be worth {value_per_year * years}")
elif years == 1:
    print(f"After {years} year, your investment will be worth {value_per_year * years}")
