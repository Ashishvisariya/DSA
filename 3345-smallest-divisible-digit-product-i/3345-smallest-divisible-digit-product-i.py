class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
         
        for i in range(n, n + 11):
            num = i
            digit_prod = 1

            while num > 0:
                digit_prod *= num % 10
                num //= 10

            if digit_prod % t == 0:
                return i