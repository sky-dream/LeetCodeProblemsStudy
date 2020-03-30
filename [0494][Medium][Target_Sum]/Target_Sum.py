# -*- coding: utf-8 -*-  
# leetcode time     cost : 88 ms
# leetcode memory   cost : 13.8 MB
# Solution 1, DP, refer to 0-1 Knapsack problem,
# 原问题转化为： 找到nums一个正子集和一个负子集，使得总和等于target，统计这种可能性的总数
# sum(P) - sum(N) = target,  
# sum(P) + sum(N) + sum(P) - sum(N) = target + sum(P) + sum(N)
# 2 * sum(P) = target + sum(nums)
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if sum(nums) < abs(S) or (sum(nums) + S) % 2 == 1: 
            return 0
        # 求出所有正子集的和
        P = (sum(nums) + S) // 2
        dp = [1] + [0 for _ in range(P)]
        for num in nums:
            for j in range(P,num-1,-1):dp[j] += dp[j - num]
        return dp[P]