# solution 3, one time traversal of the price list.
# leetcode time     cost : 72 ms
# leetcode memory   cost : 14.8 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum([y - x for x, y in zip(prices[:-1], prices[1:]) if x < y])
        #return sum(max(b-a,0)for a,b in zip(prices,prices[1:]))