class Solution:
    def lcm(self, a, b):
        return abs(a * b) // self.gcd(a, b)

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            prod = 1
            g = 0
            l = 1

            for j in range(i, n):
                x = nums[j]

                prod *= x
                g = self.gcd(g, x)
                l = self.lcm(l, x)

                if prod == g * l:
                    ans = max(ans, j - i + 1)

        return ans