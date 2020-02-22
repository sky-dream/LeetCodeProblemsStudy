# leetcode time     cost : 36 ms
# leetcode memory   cost : 13.6 MB 
# Time  Complexity: O(1)
# Space Complexity: O(1)
# solution 2, iteration
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if (n == 0): return False
        while (n & 1 == 0): n>>=1
        return n == 1;