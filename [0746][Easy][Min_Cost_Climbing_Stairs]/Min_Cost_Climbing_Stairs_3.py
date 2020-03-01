# solution 2.1, DP
class Solution:
    #def minCostClimbingStairs(self, cost: List[int]) -> int:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        # d[i] min cost before leaving i
        dp = [0 for i in range(n+1)]
        dp[0] = 0
        dp[1] = 0
        for i in range(n):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        dp[n] = min(dp[n - 1], dp[n - 2])
        return dp[n]
    
def main():
    k = 3
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]     #expect is 6
    obj = Solution()
    res = obj.minCostClimbingStairs(cost)
    print("return value is ",res);
    
if __name__ =='__main__':
    main()      