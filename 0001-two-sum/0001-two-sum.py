class Solution(object):
    def twoSum(self, nums, target):
        n = set(nums)
        for i in range(len(nums)):
            if (target - nums[i]) in n:
                for j in range(i+1,len(nums)):
                    if nums[i] + nums[j] == target:
                        return [i,j]
         