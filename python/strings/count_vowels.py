# Count the number of vowels in a string (case-insensitive)

# Input string
text = "Tokyo, Japan"

# Convert string to lowercase for case-insensitive comparison
text = text.lower()

# Vowels set
vowels = {'a', 'e', 'i', 'o', 'u'}

# Counter for vowels
vowel_count = 0

# Traverse each character in the string
for char in text:
    # Check if the character is a vowel
    if char in vowels:
        vowel_count += 1

# Print the result
print(vowel_count)

# Output:
# 4
