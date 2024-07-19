def length_of_longest_substring(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Get input from the user
s = input("Enter a string: ")

# Find the length of the longest substring without repeating characters
result = length_of_longest_substring(s)

# Print the result
print(result)
