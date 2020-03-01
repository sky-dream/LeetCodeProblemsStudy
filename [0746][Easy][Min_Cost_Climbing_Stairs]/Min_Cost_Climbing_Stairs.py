# solution 1.1, Recursion + Memorization
class Solution:
    # min cost to climb to i-th step
    def dfs_helper(self,cost,dp,i):
        if (i <= 1): 
            return 0
        if (dp[i] > 0): 
            return dp[i]
        dp[i] = min(self.dfs_helper(cost, dp, i - 1) + cost[i - 1],self.dfs_helper(cost, dp, i - 2) + cost[i - 2])
        return dp[i]

    #def minCostClimbingStairs(self, cost: List[int]) -> int:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        dp = [0 for i in range(n+1)]
        dp[n] = self.dfs_helper(cost,dp,n)
        return dp[n]
    
def main():
    k = 3
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]     #expect is 6
    obj = Solution()
    res = obj.minCostClimbingStairs(cost)
    print("return value is ",res);
    
if __name__ =='__main__':
    main()      