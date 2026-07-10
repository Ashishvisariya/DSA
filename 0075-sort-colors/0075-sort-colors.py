class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        one = 0
        zero = 0
        two = 0
        for i in nums:
            if i == 0:
                zero +=1
            elif i == 1:
                one +=1
            else:
                two +=1
        for i in range(len(nums)):
            if zero > 0:
                nums[i] = 0
                zero-=1
                continue
            elif one > 0:
                nums[i] = 1
                one-=1
                continue
            else:
                nums[i] = 2


     
            