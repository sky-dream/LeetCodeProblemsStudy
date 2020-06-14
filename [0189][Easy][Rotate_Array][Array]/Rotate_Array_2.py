# -*- coding: utf-8 -*-
# leetcode time     cost : 44 ms
# leetcode memory   cost : 14 MB 
# Time  Complexity: O(n)
# Space Complexity: O(1)
# solution 2, list concatenating
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        nums[:] = nums[-k:] + nums[:-k]