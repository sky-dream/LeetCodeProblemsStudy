# leetcode time     cost : 36 ms
# leetcode memory   cost : 13.5 MB 
# Time  Complexity: O(1)
# Space Complexity: O(1)
# solution 1, convert the num to string
class Solution:    
    #def hammingWeight(self, n: int, count = 0: int) -> int:
    def hammingWeight(self, n):
        return str('{:032b}'.format(n)).count("1")