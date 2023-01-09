"""
    1. Two Sum
    - Easy
    - LeetCode
"""

"""
    Approach 1:

def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
            try:
                index = nums.index(target-nums[i])
                if index != i:
                    return [i, index]
            except:
                pass
"""

def twoSum(nums: list[int], target: int) -> list[int]:
    table = {}
    for index, value in enumerate(nums):
        diff = target - value
        if diff in table:
            return[table[diff], index]
        else:
            table[value] = index
        
nums = list(map(int, input().split()))
target = int(input())

result = twoSum(nums, target)
print(result)
