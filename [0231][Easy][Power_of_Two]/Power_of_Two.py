# leetcode time     cost : 44 ms
# leetcode memory   cost : 13.6 MB 
# Time  Complexity: O(1)
# Space Complexity: O(1)
# solution 1, use n&(n-1 to exclude the only one lowest bit)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return 0 == n&(n-1) if n !=0 else False