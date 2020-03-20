# -*- coding: utf-8 -*-  
# leetcode time     cost : 40 ms
# leetcode memory   cost : 14.9 MB
# Time  Complexity: O(N)
# Space Complexity: O(1)
# solution 2, counter function
from collections import Counter
class Solution:
    def singleNumber(self, nums):
        hashmap = Counter(nums)
            
        for k in hashmap.keys():
            if hashmap[k] == 1:
                return k