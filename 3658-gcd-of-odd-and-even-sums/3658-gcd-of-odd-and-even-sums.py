class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        e = n*n
        o = n *(n+1)
        return gcd(e,o)
        
        