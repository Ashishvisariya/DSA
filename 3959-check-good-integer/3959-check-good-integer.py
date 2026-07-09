class Solution(object):
    def checkGoodInteger(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num = str(n)
        digit = 0
        total = 0
        for i in num:
            total += int(i)**2
            digit += int(i)
        
        return total - digit >= 50
