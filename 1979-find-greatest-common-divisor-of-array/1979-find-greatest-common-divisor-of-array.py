class Solution(object):
    def findGCD(self, nums):
        a, b = max(nums), min(nums)
        while b:
            a, b = b, a % b
        return a