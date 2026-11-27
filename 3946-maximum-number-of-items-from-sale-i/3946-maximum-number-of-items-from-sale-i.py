class Solution(object):
    def maximumSaleItems(self, items, budget):
        """
        :type items: List[List[int]]
        :type budget: int
        :rtype: int
        """
        n = len(items)
        bonus = [0]*n
        min_price =  float("inf")
        for i in range(n):
            factor_i , price_i = items[i]
            min_price = min(min_price,price_i)

            free_cnt = 0
            for j in range(n):
                if i!=j and items[j][0] % factor_i == 0:
                    free_cnt +=1
            bonus[i] = 1 + free_cnt

        dp = [-10**18]*(budget+1)
        dp[0] = 0
        for i in range(n):
            cost = items[i][1]
            
            for b in range(budget,cost-1,-1):
                dp[b] = max(dp[b],dp[b-cost]+bonus[i])
                
        ans = budget//min_price
        
        for spent in range(budget+1):
            if dp[spent] < 0:
                continue

            ans = max(ans,dp[spent]+(budget-spent)//min_price)

        return ans