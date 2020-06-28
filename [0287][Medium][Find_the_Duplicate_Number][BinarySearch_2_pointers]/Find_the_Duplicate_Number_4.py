#-*- coding: utf-8 -*-  
# leetcode time     cost : 180 ms
# leetcode memory   cost : 16 MB
# solution 2, count binary int bits
# Time  Complexity: O(NlogN)
# Space Complexity: O(1)
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums); ans = 0
        bit_max = 31
        while (((n - 1) >> bit_max) == 0):
            bit_max -= 1        
        for bit in range(bit_max+1):
            x = y = 0
            for i in range(n):
                if ((nums[i] & (1 << bit)) != 0):
                    x += 1                
                if (i >= 1 and ((i & (1 << bit)) != 0)):
                    y += 1  
            if (x > y):
                ans |= 1 << bit
        return ans