# solution 2, find all peaks and related bottom elements, then sum all peaks minus all bottoms.
# leetcode time     cost : 60 ms
# leetcode memory   cost : 15.2 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum([y for x, y, z in zip(prices[0:-1], prices[1:], prices[2:] + [prices[-1]]) if y > x and y >= z]) - \
        sum([y for x, y, z in zip([prices[0]] + prices[0:-2], prices[0:-1], prices[1:]) if y <= x and y < z]) \
        if len(prices) > 0 else 0