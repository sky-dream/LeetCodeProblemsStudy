# solution 2.1, DP
class Solution:
    #def minCostClimbingStairs(self, cost: List[int]) -> int:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        # d[i] min cost before leaving i
        dp = [0 for i in range(n+1)]
        dp[0] = 0
        dp[1] = 0
        for i in range(2,n):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        dp[n] = min(dp[n - 1], dp[n - 2])
        return dp[n]