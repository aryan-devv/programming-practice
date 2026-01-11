# Count Digits in a Number
# This program counts how many digits are present in a number
# using a while loop and integer division (Java-style logic)

# Take input from the user
num = int(input("Enter a number: "))

# Special case: if the number is 0, it has 1 digit
if num == 0:
    count = 1
else:
    count = 0

    # Loop until the number becomes 0
    while num != 0:
        num //= 10   # Remove the last digit
        count += 1  # Increase digit count

# Print the result
print("Number of digits =", count)

# Output 1:
# Enter a number: 4567
# Number of digits = 4

# Output 2:
# Enter a number: 0
# Number of digits = 1
