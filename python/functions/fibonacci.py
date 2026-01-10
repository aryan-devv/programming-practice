# Function to return the nth Fibonacci number

def fibonacci(n):
    # Handle invalid input
    if n < 0:
        return "Invalid input"

    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Initialize first two Fibonacci numbers
    a = 0
    b = 1

    # Calculate Fibonacci numbers iteratively
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


# Example input
number = 6

# Print the result
print(fibonacci(number))

# Output:
# 8
