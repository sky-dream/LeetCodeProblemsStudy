# -*- coding: utf-8 -*-  
# leetcode time     cost : 44 ms
# leetcode memory   cost : 14.7 MB
# Time  Complexity: O(N)
# Space Complexity: O(1)
# solution 3, bit operation
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_once = seen_twice = 0
        
        for num in nums:
            # first appearance: 
            # add num to seen_once 
            # don't add to seen_twice because of presence in seen_once
            
            # second appearance: 
            # remove num from seen_once 
            # add num to seen_twice
            
            # third appearance: 
            # don't add to seen_once because of presence in seen_twice
            # remove num from seen_twice
            seen_once = ~seen_twice & (seen_once ^ num)
            seen_twice = ~seen_once & (seen_twice ^ num)

        return seen_once