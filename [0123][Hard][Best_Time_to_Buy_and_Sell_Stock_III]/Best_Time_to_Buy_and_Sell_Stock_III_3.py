# solution 2, 2 times traversal.
# leetcode time     cost : 92 ms
# leetcode memory   cost : 14.4 MB 
# Time  Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        # forward traversal, profits record the max profit 
        # by the ith day, this is the first transaction
        profits = []
        max_profit = 0
        current_min = prices[0]
        for price in prices:
            current_min = min(current_min, price)
            max_profit = max(max_profit, price - current_min)
            profits.append(max_profit)
        
        # backward traversal, max_profit records the max profit
        # after the ith day, this is the second transaction 
        total_max = 0    
        max_profit = 0
        current_max = prices[-1]
        for i in range(len(prices) - 1, -1, -1):
            current_max = max(current_max, prices[i])
            max_profit = max(max_profit, current_max - prices[i])
            total_max = max(total_max, max_profit + profits[i])
            
        return total_max