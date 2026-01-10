# Find Maximum and Minimum in One Pass without using in-built functions

# Input list
numbers = [3, 1, 9, 4]

# Initialize max and min with the first element
maximum = numbers[0]
minimum = numbers[0]

# Traverse the list once
for num in numbers:
    # Update maximum if current number is greater
    if num > maximum:
        maximum = num

    # Update minimum if current number is smaller
    if num < minimum:
        minimum = num

# Print the results
print("Max =", maximum)
print("Min =", minimum)

# Output:
# Max = 9
# Min = 1
