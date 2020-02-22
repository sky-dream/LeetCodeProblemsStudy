# leetcode time     cost : 36 ms
# leetcode memory   cost : 13.5 MB 
# Time  Complexity: O(1)
# Space Complexity: O(1)
# solution 1, use n&(n-1 to exclude the only one lowest bit.
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return   n > 0 and (n & -n) == n