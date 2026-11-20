
class Solution(object):

    def find_smaller(self, A, x):
        low = 0
        high = len(A) - 1
        ans = -1

        while low <= high:
            mid = (low + high) // 2

            if A[mid] <= x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans

    def find_greater(self, A, x):
        low = 0
        high = len(A) - 1
        ans = -1

        while low <= high:
            mid = (low + high) // 2

            if A[mid] >= x:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)

        diff = float("inf")
        ans = 0

        for i in range(n):
            for j in range(i + 1, n):
                sm = nums[i] + nums[j]
                k = target - sm

                c = self.find_greater(nums, k)
                d = self.find_smaller(nums, k)

                if c != -1 and c != i and c != j:
                    total = sm + nums[c]
                    if abs(total - target) < diff:
                        diff = abs(total - target)
                        ans = total

                if d != -1 and d != i and d != j:
                    total = sm + nums[d]
                    if abs(total - target) < diff:
                        diff = abs(total - target)
                        ans = total

        return ans
