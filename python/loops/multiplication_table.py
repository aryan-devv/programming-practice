# Multiplication Table
# This program prints the multiplication table of a given number
# up to 10 using a loop and formatted output

# Take input from the user
num = int(input("Enter a number: "))

# Loop from 1 to 10
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Output:
# Enter a number: 7
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70
