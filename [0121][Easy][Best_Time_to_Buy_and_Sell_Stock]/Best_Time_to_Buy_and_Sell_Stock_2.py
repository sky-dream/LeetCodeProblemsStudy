# solution 2, one time traversal of the price list.
# leetcode time     cost : 48 ms
# leetcode memory   cost : 12.5 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy, ans = float('inf'), 0
        for p in prices:
            buy, ans = min(buy, p), max(ans, p-buy)
        return ans