# -*- coding: utf-8 -*-  
# leetcode time     cost : 40 ms
# leetcode memory   cost : 13.5 MB
# Time  Complexity: O(2**(m+n))
# Space Complexity: O(m+n)
# solution 1, brute force
class Solution:
    #def minPathSum(self, grid: List[List[int]]) -> int:
    def minPathSum(self, grid):
        return self.dfs_helper(grid, 0, 0)
    def dfs_helper(self,grid, i, j):
        if (i == len(grid) or j == len(grid[0])): 
            return float('inf')
        if (i == len(grid) - 1 and j == len(grid[0]) - 1):
            return grid[i][j]
        return grid[i][j] + min(self.dfs_helper(grid, i + 1, j), self.dfs_helper(grid, i, j + 1))


def main():
    grid = [[1,3,1],[1,5,1],[4,2,1]]       # expect is 7
    obj = Solution()
    result = obj.minPathSum(grid)
    print("return result is :",result)
    
if __name__ =='__main__':
    main()   