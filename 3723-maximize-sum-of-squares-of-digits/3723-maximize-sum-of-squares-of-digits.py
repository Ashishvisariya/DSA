
class Solution(object):
    def maxSumOfSquares(self, num, sum):
        ans = []

        if sum > 9 * num:
            return ""

        while sum > 0 and len(ans) < num:
            d = min(9, sum)
            ans.append(str(d))
            sum -= d

        while len(ans) < num:
            ans.append('0')

        return "".join(ans)
