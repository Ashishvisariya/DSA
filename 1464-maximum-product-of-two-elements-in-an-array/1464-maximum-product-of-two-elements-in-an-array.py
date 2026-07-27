class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m1 = float('-inf')
        m2 = float('-inf')
        for i in nums:
            if m1 <= i:
                m2 = m1
                m1 = i
            elif m2 <= i:
                m2 = i
            
        return (m1 - 1)*(m2-1)