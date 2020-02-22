# leetcode time     cost : 60 ms
# leetcode memory   cost : 13.6 MB 
# Time  Complexity: O(1)
# Space Complexity: O(1)
# solution 3, bit operation n&(n-1) and recursion
class Solution:    
    #def hammingWeight(self, n: int, count = 0: int) -> int:
    def hammingWeight(self, n):
        cnt = 0
        while n > 0:
            cnt += 1
            n &= n-1
        return cnt