class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p = len(nums1)
        for _ in range(p-m):
            nums1.pop()
        for j in range(n):
            nums1.append(nums2[j])
        return nums1.sort()
        