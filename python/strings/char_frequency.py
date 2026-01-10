# Count the frequency of each character in a string

# Input string
text = "programming"

# Dictionary to store character frequencies
char_frequency = {}

# Traverse each character in the string
for char in text:
    # If character already exists in dictionary, increment count
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        # Otherwise, add character with count 1
        char_frequency[char] = 1

# Print the frequency dictionary
print(char_frequency)

# Output:
# {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}
