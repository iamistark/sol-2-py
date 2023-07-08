def findLHS(nums):
    num_count = {}
    max_length = 0

    # Count the occurrences of each number
    for num in nums:
        num_count[num] = num_count.get(num, 0) + 1

    # Check each number in the dictionary
    for num in num_count:
        if num + 1 in num_count:
            length = num_count[num] + num_count[num + 1]
            max_length = max(max_length, length)

    return max_length
#Driver code
nums = [1, 3, 2, 2, 5, 2, 3, 7]
print(findLHS(nums))
