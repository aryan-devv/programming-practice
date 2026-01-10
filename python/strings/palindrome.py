# Check if a string is a palindrome

# Input string
text = "level"

# Assume the string is a palindrome
is_palindrome = True

# Compare characters from start and end
for i in range(len(text) // 2):
    if text[i] != text[len(text) - 1 - i]:
        is_palindrome = False
        break

# Print the result
print(is_palindrome)

# Output:
# True
