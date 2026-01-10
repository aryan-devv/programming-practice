# Function to calculate the sum of digits of a number

def sum_of_digits(n):
    # Handle negative numbers
    n = abs(n)

    total = 0

    # Extract digits one by one
    while n > 0:
        digit = n % 10       # Get last digit
        total += digit       # Add digit to total
        n //= 10             # Remove last digit

    return total


# Example input
number = 1234

# Print the result
print(sum_of_digits(number))

# Output:
# 10
