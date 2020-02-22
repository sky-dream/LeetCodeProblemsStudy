# leetcode time     cost : 40 ms
# leetcode memory   cost : 13.6 MB 
# Time  Complexity: O(1)
# Space Complexity: O(1)
# solution 2, bit operation 
class Solution:    
    #def hammingWeight(self, n: int, count = 0: int) -> int:
    def hammingWeight(self,n):
        r = 0
        while n:
            if n & 1:
                r += 1
            n >>= 1
        return r 