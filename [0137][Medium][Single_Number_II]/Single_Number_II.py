# -*- coding: utf-8 -*-  
# leetcode time     cost : 50 ms
# leetcode memory   cost : 15 MB
# Time  Complexity: O(1)
# Space Complexity: O(1)
# solution 1, calculate the sum of nums and 3 times sum of every num, only 1 num appear once
class Solution:
    def singleNumber(self, nums):
        return (3 * sum(set(nums)) - sum(nums)) // 2