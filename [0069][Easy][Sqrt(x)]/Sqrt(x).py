# solution 1, e and log,
# leetcode time     cost : 40 ms
# leetcode memory   cost : 13 MB 
# Time  Complexity: O(1)
# Space Complexity: O(1)
from math import e, log
class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x
        
        left = int(e**(0.5 * log(x)))
        right = left + 1
        return left if right * right > x else right