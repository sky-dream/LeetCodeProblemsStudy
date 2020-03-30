# -*- coding: utf-8 -*-  
# leetcode time     cost : 1688 ms
# leetcode memory   cost : 19.4 MB
# raw DP, slow,
# dp[(i,j)]=dp.get((i−1,j−nums[i]),0)+dp.get((i−1,j+nums[i]),0)
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        length, dp = len(nums), {(0,0): 1}
        for i in range(1, length+1):
            for j in range(-sum(nums), sum(nums) + 1):
                dp[(i,j)] = dp.get((i - 1, j - nums[i-1]), 0) + dp.get((i - 1, j + nums[i-1]), 0)             
        return dp.get((length, S), 0)