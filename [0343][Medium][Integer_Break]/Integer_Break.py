# solution 1, analysis.
# leetcode time     cost : 36 ms
# leetcode memory   cost : 13.1 MB 
# Time  Complexity: O(1)
# Space Complexity: O(1)
class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3: return n - 1
        a, b = n // 3, n % 3
        if b == 0: return pow(3, a)
        if b == 1: return pow(3, a - 1) * 4
        #else b==2
        return pow(3, a) * 2 