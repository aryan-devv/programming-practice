# Sum of First N Natural Numbers
# This program calculates the sum of numbers from 1 to N
# using the accumulation pattern

# Take input from the user
N = int(input("Enter a number: "))

# Variable to store the sum
total = 0

# Loop from 1 to N and add each number to total
for i in range(1, N + 1):
    total += i

# Print the final result
print("Sum =", total)

# Output:
# Enter a number: 5
# Sum = 15
