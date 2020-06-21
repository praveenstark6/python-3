def two_sum(nums: list, target: int) -> list:
    for i in range(len(nums)):
        num = target-nums[i]
        if num in nums and i != nums.index(num):
            return [i, nums.index(num)]


print(two_sum([3,2,95,4,-3], 92))