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