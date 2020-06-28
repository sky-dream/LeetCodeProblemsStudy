#-*- coding: utf-8 -*-  
# leetcode time     cost : 104 ms
# leetcode memory   cost : 16 MB
# solution 1, binary search
# Time  Complexity: O(NlogN)
# Space Complexity: O(1)
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)-1
        left,right = 1,n+1
        
        while left+1<right:
            mid = left + (right-left)//2
            #count the nums between left and mid,check whether more than (mid-left+1).
            counter = 0
            for i in range(n+1):
                if left<=nums[i]<mid:
                    counter += 1
                    
            if counter > (mid-left):
                right = mid
            else:
                left = mid
        return left