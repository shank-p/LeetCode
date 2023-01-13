"""
    26. Remove Duplicates from Sorted Array
    - easy
    - LeetCode
"""
"""
    Approach 1:

def removeDuplicates(nums: list[int]) -> int:
    n = len(nums)
    prev = nums[0]
    i = 1
    nums.append(-1)
    while (i < n):
        if prev == nums[i]:
            nums.insert(n, nums.pop(i))
            print(nums)
        elif prev < nums[i]:
            prev = nums[i]
            i += 1
        else:
            return i
    return i
"""

def removeDuplicates(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1

nums = list(map(int, input().split()))
result = removeDuplicates(nums)
print(result)