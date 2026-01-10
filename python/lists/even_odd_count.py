# Count Even and Odd Numbers in a List

# Input list
numbers = [1, 2, 3, 4, 6]

# Initialize counters
even_count = 0
odd_count = 0

# Traverse the list
for num in numbers:
    # Check if the number is even
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Print the results
print("Even =", even_count)
print("Odd =", odd_count)

# Output:
# Even = 3
# Odd = 2
