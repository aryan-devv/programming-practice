# Prime Number Check
# This program checks whether a given number is a prime number
# using loops and conditional statements

# Take input from the user
num = int(input("Enter a number: "))

# Prime numbers are greater than 1
if num <= 1:
    print("Not a Prime Number")
else:
    is_prime = True

    # Check divisibility from 2 to num-1
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    # Print result based on the flag
    if is_prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")

# Output 1:
# Enter a number: 13
# Prime Number

# Output 2:
# Enter a number: 15
# Not a Prime Number

# Output 3:
# Enter a number: 1
