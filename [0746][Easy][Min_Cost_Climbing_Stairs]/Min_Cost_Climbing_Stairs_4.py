# solution 2.3, DP
class Solution:
    #def minCostClimbingStairs(self, cost: List[int]) -> int:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        # dp[i] : min cost to climb to n-th step
        one_step_before = 0
        two_step_before = 0
        for i in range(2,n+1):
            dp_i = min(one_step_before + cost[i-1], two_step_before + cost[i-2])
            two_step_before = one_step_before
            one_step_before = dp_i
        return dp_i
    
def main():
    k = 3
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]     #expect is 6
    obj = Solution()
    res = obj.minCostClimbingStairs(cost)
    print("return value is ",res);
    
if __name__ =='__main__':
    main()      