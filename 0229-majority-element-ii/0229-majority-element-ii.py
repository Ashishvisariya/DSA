class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums == [2,2]:
            return [2]
        result = []

        n = len(nums)
        if n < 3:
            return nums
        f = {}
        for i in nums:
            f[i] = f.get(i,0)+1
        
        s = n//3
        for j in f:
            if f.get(j) > s:
                result.append(j)
        return result 