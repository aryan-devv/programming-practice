# Reverse a string without using slicing

# Input string
text = "Tokyo, Japan"

# Empty string to store the reversed result
reversed_text = ""

# Traverse the string from end to start
for i in range(len(text) - 1, -1, -1):
    reversed_text += text[i]

# Print the reversed string
print(reversed_text)

# Output: napaJ ,oykoT
