# Function to calculate factorial using a loop

def factorial(n):
    # Factorial of negative numbers is not defined
    if n < 0:
        return "Factorial not defined for negative numbers"

    result = 1

    # Multiply numbers from 1 to n
    for i in range(1, n + 1):
        result *= i

    return result


# Example input
number = 5

# Print the result
print(factorial(number))

# Output:
# 120
