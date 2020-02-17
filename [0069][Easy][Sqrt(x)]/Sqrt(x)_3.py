# solution 3, bit op and recursion,
# leetcode time     cost : 40 ms
# leetcode memory   cost : 13.1 MB 
# Time  Complexity: O(logN)
# Space Complexity: O(logN)
class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x
        
        left = self.mySqrt(x >> 2) << 1
        right = left + 1
        return left if right * right > x else right