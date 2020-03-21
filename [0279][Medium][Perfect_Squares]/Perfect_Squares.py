#-*- coding: utf-8 -*-  
# leetcode time     cost : maximum recursion depth exceeded in comparison
# leetcode memory   cost : --- MB
# Time  Complexity: O(N)
# Space Complexity: O(N)
# solution 1, back track
class Solution:
    def numSquares(self, n: int) -> int:
        visited ={}
        self.numSquaresHelper(n, visited)
        
    def numSquaresHelper(self,n, visited):
        if (n in visited):
            return visited[n]
        if (n == 0):
            return 0
        
        count = float('inf')
        
        for i in range(n):
            if i*i<=n:  #i - j * j >= 0
                count = min(count, self.numSquaresHelper(n - i*i, visited) + 1)
            else:
                break
        map[n] = count
        return count