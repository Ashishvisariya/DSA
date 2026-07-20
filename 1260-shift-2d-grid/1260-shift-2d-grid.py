class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        for _ in range(k):
            for i in range(len(grid)):
                grid[i] = [grid[i-1].pop()] + grid[i]
        return grid

            
                