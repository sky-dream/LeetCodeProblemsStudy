#-*- coding: utf-8 -*-  
# leetcode time     cost : 80 ms
# leetcode memory   cost : 19.2 MB
# Time  Complexity: O(N)
# Space Complexity: O(N)
# solution 1, Recursion.
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        if n==0:
            return []
        helperResult = self.helper(n)
        result = []
        for char in helperResult:
            # remove char start with "0"
            if len(str(int(char))) == n:
                result.append(char)
        return result
        
    def helper(self,n):
        if n==1:
            return ["0","1","8"]
        if n==2:
            # need include 00 and remove start with 0 at last
            return ["00","11","69","88","96"]
        subResult = self.helper(n-2)
        result = []
        for char in subResult:
            for deltaChar in ["00","11","69","88","96"]:
                
                result.append(deltaChar[0]+char+deltaChar[1])
        return result