class Solution(object):
    def gcdValues(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        maxE = max(nums)

        freq = [0] * (maxE + 1)
        for num in nums:
            freq[num] += 1

        exact = [0] * (maxE + 1)

        for gcd in range(maxE, 0, -1):
            cnt = 0

            for times in range(gcd, maxE + 1, gcd):
                cnt += freq[times]

            exact[gcd] = cnt * (cnt - 1) // 2

            for times in range(2 * gcd, maxE + 1, gcd):
                exact[gcd] -= exact[times]

        pref = [0] * (maxE + 1)
        for gcd in range(1, maxE + 1):
            pref[gcd] = pref[gcd - 1] + exact[gcd]

        result = []
        for q in queries:
            left, right = 1, maxE
            while left < right:
                mid = (left + right) // 2
                if pref[mid] > q:
                    right = mid
                else:
                    left = mid + 1
            result.append(left)

        return result



        