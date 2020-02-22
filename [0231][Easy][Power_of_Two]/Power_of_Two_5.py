# leetcode time     cost : 60 ms
# leetcode memory   cost : 13.6 MB 
# Time  Complexity: O(1)
# Space Complexity: O(1)
# solution 3, recursion
class Solution:
    def isPowerOfTwo(self, n: int):
        return n > 0 and (n == 1 or (n&1 == 0 and self.isPowerOfTwo(n>>1)))