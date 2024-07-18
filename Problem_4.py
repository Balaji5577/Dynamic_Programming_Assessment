def max_subarray_sum(nums):
    # Initialize the variables
    max_current = nums[0]
    max_global = nums[0]

    for i in range(1, len(nums)):
        max_current = max(nums[i], max_current + nums[i])
        if max_current > max_global:
            max_global = max_current

    return max_global

# Read input from the user
nums = list(map(int, input().strip().split()))

# Find the subarray with the largest sum
result = max_subarray_sum(nums)

# Print the result
print(result)
