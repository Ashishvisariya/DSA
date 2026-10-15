class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                total += len(set(nums[i:j]))**2
        return total
