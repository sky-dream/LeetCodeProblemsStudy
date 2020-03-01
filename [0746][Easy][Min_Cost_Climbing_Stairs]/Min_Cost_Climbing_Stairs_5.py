# solution 2.2, DP
class Solution:
    #def minCostClimbingStairs(self, cost: List[int]) -> int:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        # dp[i] : min cost to climb to n-th step
        dp = [0 for i in range(n+1)]
        dp[0] = 0
        dp[1] = 0
        for i in range(2,n+1):
            dp[i] = min(dp[i - 1] + cost[i-1], dp[i - 2] + cost[i-2])
        return dp[n]
    
def main():
    k = 3
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]     #expect is 6
    obj = Solution()
    res = obj.minCostClimbingStairs(cost)
    print("return value is ",res);
    
if __name__ =='__main__':
    main()      