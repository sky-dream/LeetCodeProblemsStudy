# leetcode time     cost : 40 ms
# leetcode memory   cost : 13.6 MB 
# Time  Complexity: O(1)
# Space Complexity: O(1)
# solution 2, bit operation
class Solution:
    def hammingWeight(self, n: int) -> int:
        return len([i for i in range(32) if (1<<i)&n])  