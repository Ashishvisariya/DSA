class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = float('-inf')
        max2 = float('-inf')
        
        for num in nums:
            if max1 <= num:
                max2 = max1
                max1 = num
            elif max2 <= num:
                max2 = num
        return (max1-1)*(max2-1)