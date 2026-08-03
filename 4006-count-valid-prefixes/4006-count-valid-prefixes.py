class Solution(object):
    def countValidPrefixes(self, s):
        """
        :type s: str
        :rtype: int
        """
        zero = 0
        one = 0
        ans = 0

        for ch in s:
            if ch == '0':
                zero += 1
            else:
                one += 1

            if abs(zero - one) <= 1:
                ans += 1

        return ans
                