class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 0:
            return n
        return self.fib(n-1)+self.fib(n-2)