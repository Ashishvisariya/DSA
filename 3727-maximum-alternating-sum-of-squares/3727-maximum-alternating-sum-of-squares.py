
class Solution(object):
    def maxAlternatingSum(self, nums):
        f = sorted(abs(i) for i in nums)
        n = len(f)
        x = n // 2

        s = 0
        for i in range(x):
            s -= f[i] * f[i]
        
        for i in range(x, n):
            s += f[i] * f[i]

        return s
