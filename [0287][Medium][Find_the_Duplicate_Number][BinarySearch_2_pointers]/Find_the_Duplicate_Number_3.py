#-*- coding: utf-8 -*-  
# leetcode time     cost : 152 ms
# leetcode memory   cost : 15.8 MB
# solution 1, binary search
# Time  Complexity: O(NlogN)
# Space Complexity: O(1)
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l = 1; r = n - 1;ans = -1
        while (l <= r):
            mid = (l + r) >> 1
            cnt = 0
            for i in range(n):
                if (nums[i] <= mid):
                    cnt+=1
            if (cnt <= mid):
                l = mid + 1
            else: 
                r = mid - 1
                ans = mid
        return ans