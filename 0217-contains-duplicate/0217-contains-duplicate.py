class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        my_set = set(nums)
        if len(nums) != len(my_set):
            return True
        else:
            return False