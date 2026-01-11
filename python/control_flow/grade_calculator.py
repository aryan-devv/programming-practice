# Grade Calculator
# This program takes marks (0–100) as input
# and prints the corresponding grade using range-based logic

# Take input from the user
marks = int(input("Enter marks (0-100): "))

# Check if marks are within valid range
if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Grade: Fail")

# Output 1:
# Enter marks (0-100): 92
# Grade: A

# Output 2:
# Enter marks (0-100): 68
# Grade: C

# Output 3:
# Enter marks (0-100): 33
# Grade: Fail
