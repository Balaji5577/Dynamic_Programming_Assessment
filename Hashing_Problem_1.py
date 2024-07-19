def two_sum(nums, target):
    num_to_index = {}  # Dictionary to store the index of each number we have seen
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index
    return []  # If no solution is found

# Example usage
nums = list(map(int, input().split()))
target = int(input())
print(two_sum(nums, target))  # Output: [0, 1]
