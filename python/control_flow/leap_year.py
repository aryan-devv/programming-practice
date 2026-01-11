# Leap Year Checker
# This program checks whether a given year is a leap year
# using compound logical conditions

# Take input from the user
year = int(input("Enter a year: "))

# Check leap year conditions
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# Output 1:
# Enter a year: 2024
# Leap Year

# Output 2:
# Enter a year: 1900
# Not a Leap Year

# Output 3:
# Enter a year: 2000
# Leap Year
