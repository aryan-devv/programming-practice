# Find the Second Largest Distinct Element in a List
# Without using sorting

# Input list
numbers = [10, 5, 8, 10]

# Initialize largest and second largest
largest = None
second_largest = None

# Traverse the list
for num in numbers:
    # Update largest and second largest
    if largest is None or num > largest:
        if num != largest:
            second_largest = largest
        largest = num

    # Update second largest if needed
    elif num != largest and (second_largest is None or num > second_largest):
        second_largest = num

# Check if second largest exists
if second_largest is None:
    print("No second largest element found")
else:
    print("Second Largest =", second_largest)

# Output:
# Second Largest = 8
