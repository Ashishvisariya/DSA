class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        n = len(nums)
        total = 1<<n

        for num in range(total):
            pack = []
            for i in range(0,n):
                if num & (1<<i)!= 0:

                    pack.append(nums[i])
            result.append(pack)
        return result 
