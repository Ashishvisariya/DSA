class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        t = 0
        result = []
        num = str(n)
        for i in num:
            if i != '0':
                result.append(i)
                t += int(i)
        return int("".join(result))*t




        