class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x = n
        p = 1
        s = 0
        while n > 0:
            r = n%10
            s += r
            p*=r
            n//=10
        m = s + p
        if x % m == 0:
            return True
        else:
            return False