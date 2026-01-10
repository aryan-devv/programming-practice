'''This program takes an list and reverses it'''

# Method 1
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list1.reverse()
print(list1)

# Method 2
list2 = [2, 3, 6, 2, 8, 3, 6, 5]
print(list2[::-1])

# Method 3
list3 = [2, 5, 3, 7, 2, 6, 4, 7]

left = 0
right = len(list3) - 1

while left < right:
    list3[left], list3[right] = list3[right], list3[left]
    left += 1
    right -= 1

print(list3)

# There are many other ways to reverse a list but these are the most popular and easy to read

# Output:
# [8, 7, 6, 5, 4, 3, 2, 1]
# [5, 6, 3, 8, 2, 6, 3, 2]
# [7, 4, 6, 2, 7, 3, 5, 2]
