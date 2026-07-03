class Solution(object):
    def findDegrees(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n = len(matrix)
        ans = []

        for i in range(n):
            ans.append(sum(matrix[i]))

        return ans