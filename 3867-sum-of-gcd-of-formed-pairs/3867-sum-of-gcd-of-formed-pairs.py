class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        p_grid = []
        m_num = float('-inf')
        for i in range(len(nums)):
            m_num = max(m_num,nums[i])
            p_grid.append(gcd(m_num,nums[i]))
        p_grid.sort()

        i = 0 
        j = len(p_grid)-1
        t = 0
        while i < j:
            t+= gcd(p_grid[i],p_grid[j])
            i+=1
            j-=1
        return t



        