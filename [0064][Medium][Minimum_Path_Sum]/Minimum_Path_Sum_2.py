# -*- coding: utf-8 -*-  
# leetcode time     cost : 60 ms
# leetcode memory   cost : 15.1 MB
# Time  Complexity: O(m*n)
# Space Complexity: O(n)
# solution 2, 2 dimesion DP
class Solution:
    #def minPathSum(self, grid: List[List[int]]) -> int:
    def minPathSum(self, grid):
        m,n = len(grid),len(grid[0])
        dp = [[0 for i in range(n) ] for i in range(m)]
        for i  in range(m-1,-1,-1):
            for j  in range(n-1,-1,-1):
                if(i == m - 1 and j != n - 1):
                    dp[i][j] = grid[i][j] +  dp[i][j + 1]
                elif(j == n - 1 and i != m - 1):
                    dp[i][j] = grid[i][j] + dp[i + 1][j]
                elif(j != n - 1 and i != m - 1):
                    dp[i][j] = grid[i][j] + min(dp[i + 1][j], dp[i][j + 1])
                else:
                    dp[i][j] = grid[i][j]     
        return dp[0][0]
    
    def minPathSum_2(self, grid):
        m,n = len(grid),len(grid[0])
        dp = [[0 for i in range(n) ] for i in range(m)]
        for i  in range(m):
            for j  in range(n):
                if(i == 0 and j != 0):
                    dp[i][j] = grid[i][j] +  dp[i][j - 1]
                elif(j == 0 and i != 0):
                    dp[i][j] = grid[i][j] + dp[i - 1][j]
                elif(j != 0 and i != 0):
                    dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
                else:
                    dp[i][j] = grid[i][j]       
        return dp[m-1][n-1]

def main():
    grid = [[1,2],[5,6],[1,1]]      # expect is 7
    obj = Solution()
    result = obj.minPathSum_2(grid)
    print("return result is :",result)
    
if __name__ =='__main__':
    main()    