# Function to check if a number is prime

def is_prime(n):
    # Prime numbers must be greater than 1
    if n <= 1:
        return False

    # Check divisibility up to square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


# Example input
number = 7

# Print the result
print(is_prime(number))


# Output:
# True
