# solution 3, one time traversal of the price list.
# leetcode time     cost : 44 ms
# leetcode memory   cost : 12.7 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))