# -*- coding: utf-8 -*-
# leetcode time     cost : 40 ms
# leetcode memory   cost : 13.8 MB 
# Time  Complexity: O(n)
# Space Complexity: O(1)
# solution 3, reverse 3 times
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        # example: [1,2,3,4,5,6,7],k=3
        nums[:n-k] = nums[:n-k][::-1]   # [4,3,2,1,5,6,7]
        nums[n-k:] = nums[n-k:][::-1]   # [4,3,2,1,7,6,5]
        nums[:] = nums[::-1]        # [5,6,7,1,2,3,4]