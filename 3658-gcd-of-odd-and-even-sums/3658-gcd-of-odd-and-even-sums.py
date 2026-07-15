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
        e_sum = 0
        o_sum = 0
        e_count = 0
        o_count = 0
        i = 1
        while o_count < n and e_count < n:
            if i % 2 != 0:
                o_sum += i
                o_count+=1
            else:
                e_sum += i
                e_count+=1
            i+=1
                
        return gcd(e_sum,o_sum)

        