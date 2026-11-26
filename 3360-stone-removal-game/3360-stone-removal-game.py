class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        m=10
        t=0
        while n>=m:
            n-=m
            m-=1
            t=1-t
        return t!=0