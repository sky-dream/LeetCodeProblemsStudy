# solution 4, Integer Newton,
# leetcode time     cost : 36 ms
# leetcode memory   cost : 13.1 MB 
# Time  Complexity: O(logN)
# Space Complexity: O(1)
class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x
        
        x0 = x
        x1 = (x0 + x / x0) / 2
        while abs(x0 - x1) >= 1:
            x0 = x1
            x1 = (x0 + x / x0) / 2        
            
        return int(x1)