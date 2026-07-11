class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_list = {}
        for i in nums:
            my_list[i] = my_list.get(i,0)+1

        return max(my_list ,key=my_list.get)