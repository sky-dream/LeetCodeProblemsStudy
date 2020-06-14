# -*- coding: utf-8 -*-
# leetcode time     cost : 136 ms
# leetcode memory   cost : 13.9 MB 
# Time  Complexity: O(k)
# Space Complexity: O(n)
# solution 1, pop the right side element insert into the left
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        for _ in range(k):
            nums.insert(0, nums.pop())