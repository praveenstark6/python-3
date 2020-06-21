"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""
numbers = list(map(int,input().split()))
target_number = int(input())

def two_sum(nums: list, target: int) -> list:
    for i in range(len(nums)):
        num = target-nums[i]
        if num in nums and i != nums.index(num):
            return [i, nums.index(num)]

print(two_sum(numbers, target_number))
