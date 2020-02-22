# leetcode time     cost : 40 ms
# leetcode memory   cost : 13.5 MB 
# Time  Complexity: O(1)
# Space Complexity: O(1)
# solution 1, convert the num to binary string
class Solution:
    def hammingWeight(self, n: int) -> int:
        return str(bin(n)[2:]).count('1')