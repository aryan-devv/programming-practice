# Reverse a Number
# This program takes a number as input
# and prints its reverse using math and loop logic

# Take input from the user
num = int(input("Enter a number: "))

# Variable to store the reversed number
reverse = 0

# Loop until the number becomes 0
while num != 0:
    digit = num % 10        # Get the last digit
    reverse = reverse * 10 + digit
    num //= 10              # Remove the last digit

# Print the reversed number
print("Reversed number =", reverse)

# Output 1:
# Enter a number: 123
# Reversed number = 321

# Output 2:
# Enter a number: 9070
# Reversed number = 709
