# -*- coding: utf-8 -*-  
# leetcode time     cost : 6920 ms
# leetcode memory   cost : 13.6 MB
# Time  Complexity: O(M*N*N)
# Space Complexity: O(M*N)
# solution 2, DP
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        presum = [0 for i in range(len(nums))]
        presum[0] = nums[0]
        for i in range(1, len(nums)):
            presum[i] =  presum[i-1]  + nums[i]    
        # presum[j] - presum[i] = [i+1, j]
        
        # f[i][j]表示从nums[0]~nums[j]分成i组的解
        f = [[float('inf')] * len(nums) for i in range(m+1)]
        # f[1][j] = sum(0, j), 包含边界，表示只划分一段时的解
        for j in range(len(nums)):
            f[1][j] = presum[j]
            
        for i in range(2, m + 1):
            for j in range(i - 1, len(nums)):
                for k in range(0, j):
                    f[i][j] = min(f[i][j], max(f[i-1][k], presum[j] - presum[k]))
        return f[m][len(nums)-1]