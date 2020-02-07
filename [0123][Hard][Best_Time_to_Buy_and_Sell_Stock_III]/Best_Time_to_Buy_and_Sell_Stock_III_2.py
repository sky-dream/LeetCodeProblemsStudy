# solution 1, DP simplified version.
# dp general version pls refer to java 1 version.
# leetcode time     cost : 3 ms
# leetcode memory   cost : 36.8 MB 
# Time  Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dynamic programming
        first_buy, first_profit, second_buy_first_porfit, max_profit = float('inf'), 0, float('inf'), 0
        for price in prices:
            first_buy = min(first_buy, price)
            first_profit = max(first_profit, price-first_buy)
            second_buy_first_porfit = min(second_buy_first_porfit, price-first_profit)
            max_profit = max(max_profit, price-second_buy_first_porfit)
        return max_profit