# Print Numbers from 1 to N
# This program takes an integer N as input
# and prints numbers from 1 to N using a loop

# Take input from the user
N = int(input("Enter a number: "))

# Loop from 1 to N (inclusive)
print("Using for loop: ")
for i in range(1, N + 1):
    print(i)

print("Using while loop: ")
i = 1
while i <= N:
    print(i)
    i += 1

# Output:
# Enter a number: 5
# Using for loop:
# 1
# 2
# 3
# 4
# 5
# Using while loop:
# 1
# 2
# 3
# 4
# 5
