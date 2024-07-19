def group_anagrams(strs):
    anagrams = {}
    for s in strs:
        sorted_s = tuple(sorted(s))
        if sorted_s in anagrams:
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]
    return list(anagrams.values())

# Get input from the user
strs = input().split()

# Group the anagrams
result = group_anagrams(strs)

# Print the result
for group in result:
    print(group)
