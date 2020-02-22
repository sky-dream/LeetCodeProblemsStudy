# leetcode time     cost : 36 ms
# leetcode memory   cost : 13.5 MB 
# Time  Complexity: O(1)
# Space Complexity: O(1)
# solution 3, bit operation n&(n-1) and recursion
class Solution:    
    #def hammingWeight(self, n: int, count = 0: int) -> int:
    def hammingWeight(self, n, count = 0):
        return self.hammingWeight(n & n-1, count+1) if n!=0 else count  