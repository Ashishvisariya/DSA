class Solution(object):
    def uniformArray(self, nums1):
        mn = min(nums1)
        if mn % 2 !=0:
            return True
        else:
            for i in range(len(nums1)):
                if nums1[i] % 2 != 0:
                    return False
        return True

        