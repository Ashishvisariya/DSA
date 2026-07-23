class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)        
        return 1 << (n.bit_length() - 3 // (n + 1))