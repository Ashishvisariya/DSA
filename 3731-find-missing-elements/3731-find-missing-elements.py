class Solution(object):
    def findMissingElements(self, nums):
        present = [False] * 102  # fixed size, bounded by constraint (values 1..100)

        lo, hi = min(nums), max(nums)

        for num in nums:
            present[num] = True

        missing = []

        for v in range(lo, hi + 1):
            if not present[v]:
                missing.append(v)

        return missing