def minimumScore(nums, k):
    nums.sort()  
    min_val = nums[0]  
    max_val = nums[-1]

    
    for i in range(len(nums) - 1):
        min_val = min(min_val, nums[i + 1] - k)
        max_val = max(max_val, nums[i] + k)

    return max(0, max_val - min_val)

#Driver code
nums = [1]
k = 0
print(minimumScore(nums, k))

