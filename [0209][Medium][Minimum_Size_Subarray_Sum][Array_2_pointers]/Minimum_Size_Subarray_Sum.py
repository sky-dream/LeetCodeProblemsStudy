#-*- coding: utf-8 -*- 
# solution 1, brute force 
# Time  Complexity: O(N*N)
# Space Complexity: O(1)
from typing import List
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        ans = n + 1
        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                if total >= s:
                    ans = min(ans, j - i + 1)
                    break
        
        return 0 if ans == n + 1 else ans