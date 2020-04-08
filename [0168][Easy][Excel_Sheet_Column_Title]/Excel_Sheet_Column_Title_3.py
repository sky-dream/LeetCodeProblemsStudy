# leetcode time     cost : 40 ms
# leetcode memory   cost : 13.6 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def convertToTitle(self, n: int) -> str:
        # A ascii is 65
        return "" if n == 0 else self.convertToTitle((n - 1) // 26) + chr((n - 1) % 26 + 65)