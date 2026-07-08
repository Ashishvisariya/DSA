class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        for num in range(len(nums)):
            if nums[num] != 0:
                nums[i],nums[num] = nums[num],nums[i]
                i+=1