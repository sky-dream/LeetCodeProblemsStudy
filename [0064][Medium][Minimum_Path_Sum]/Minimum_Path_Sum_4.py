# -*- coding: utf-8 -*-  
# leetcode time     cost : 56 ms
# leetcode memory   cost : 14.6 MB
# Time  Complexity: O(m*n)
# Space Complexity: O(n)
# solution 4, 1 dimesion DP with no extral storage space
class Solution:
    #def minPathSum(self, grid: List[List[int]]) -> int:
    def minPathSum(self, grid):
        m,n = len(grid),len(grid[0])
        for i  in range(m):
            for j  in range(n):
                if(i == 0 and j != 0):
                   grid[i][j] = grid[i][j] +  grid[i][j-1]
                elif(j == 0 and i != 0):
                   grid[i][j] = grid[i-1][j] + grid[i][j]
                elif(j != 0 and i != 0):
                   grid[i][j] = grid[i][j] + min(grid[i-1][j], grid[i][j-1])
                else:
                   grid[i][j] = grid[i][j]              
        return grid[m-1][n-1]


def main():
    grid = [[1,3,1],[1,5,1],[4,2,1]]       # expect is 7
    obj = Solution()
    result = obj.minPathSum(grid)
    print("return result is :",result)
    
if __name__ =='__main__':
    main()    