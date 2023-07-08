def arrayPairSum(nums):
    nums.sort()  # Sort the array in ascending order
    max_sum = 0
    for i in range(0, len(nums), 2):
        max_sum += nums[i]  # Add the minimum element in each pair
    return max_sum
#Driver code
nums = [1, 4, 3, 2]
print(arrayPairSum(nums))
