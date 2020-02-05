# solution 2, one time traversal of the price list.
# leetcode time     cost : 56 ms
# leetcode memory   cost : 12.5 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit