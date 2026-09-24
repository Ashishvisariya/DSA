class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            t = 0
            while nums[i] > 0:
                t += nums[i] % 10
                nums[i] /= 10
            if t == i:
                return i
        return -1
            