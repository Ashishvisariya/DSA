class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = []
        while n > 0:
            r = n % 10
            m.append(r)
            n//=10
        m.sort()
        return m[-1]*m[-2]
