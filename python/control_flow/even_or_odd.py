# Even or Odd Checker
# This program takes an integer input and checks
# whether the number is Even or Odd using modulo operator

# Take input from the user
number = int(input("Enter an integer: "))

# Check if the number is even or odd
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Output 1:
# Enter an integer: 6
# Even

# Output 2:
# Enter an integer: 7
# Odd
