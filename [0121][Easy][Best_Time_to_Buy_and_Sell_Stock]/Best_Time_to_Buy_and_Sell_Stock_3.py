# solution 3, DP.
# leetcode time     cost : 100 ms
# leetcode memory   cost : 16.5 MB 
# Time  Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        res = 0
        profit = [[0 for i in range(3)] for i in range(len(prices))] 
        profit[0][0], profit[0][1], profit[0][2] = 0, -prices[0], 0
        # i is the day, k is the transaction status.
        for i in range(1,len(prices)):
            #has no stock
            profit[i][0] = profit[i-1][0] 
            #buy the stock     
            profit[i][1] = max (profit[i-1][1],profit[i-1][0] - prices[i]) 
            #sell the stock     
            profit[i][2] = profit[i-1][1] + prices[i]
            #get max profit in all cases       
            res = max(res, profit[i][0], profit[i][1], profit[i][2])
        return res
    
    def maxProfit_2(self, prices: List[int]) -> int:
        if not prices or len(prices)==1:
            return 0
        n = len(prices)
        dp = [[0 for i in range(2)] for j in range(n)]
        # dp[i][0] is the profit if day i-th has 0 stock, res is dp[n-1][0]
        # dp[i][1] is the profit if day i-th has 1 stock
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        # check from 1-th day to n-th day
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
            # due to we can only have 1 transaction,so the profit of i-day with stock is just the -prices[i],
            dp[i][1] = max(dp[i-1][1],-prices[i]) 
        return dp[n-1][0]