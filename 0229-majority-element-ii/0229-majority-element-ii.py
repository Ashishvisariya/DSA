class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        n = len(nums)
        f = {}
        for i in nums:
            f[i] = f.get(i, 0) + 1
        s = n // 3
        for j in f:
            if f[j] > s:
                result.append(j)

        return result
            