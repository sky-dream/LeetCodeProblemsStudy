# -*- coding: utf-8 -*-  
# leetcode time     cost : 32 ms
# leetcode memory   cost : 13.6 MB
# Time  Complexity: O(m*n)
# Space Complexity: O(n)
# solution 3, 1 dimesion DP
class Solution:
    #def minPathSum(self, grid: List[List[int]]) -> int:
    def minPathSum(self, grid):
        m,n = len(grid),len(grid[0])
        dp = [0 for i in range(n)]
        for i  in range(m):
            for j  in range(n):
                if(i == 0 and j != 0):
                   dp[j] = grid[i][j] +  dp[j - 1]
                elif(j == 0 and i != 0):
                   dp[j] = grid[i][j] + dp[j]
                elif(j != 0 and i != 0):
                   dp[j] = grid[i][j] + min(dp[j], dp[j - 1])
                else:
                   dp[j] = grid[i][j]              
        return dp[n-1]

    def minPathSum_2(self, grid):
        m,n = len(grid),len(grid[0])
        dp = [0 for i in range(n)]
        for i  in range(m-1,-1,-1):
            for j  in range(n-1,-1,-1):
               if(i == m - 1 and j != n - 1):
                   dp[j] = grid[i][j] +  dp[j + 1];
               elif(j == n - 1 and i != m - 1):
                   dp[j] = grid[i][j] + dp[j];
               elif(j != n - 1 and i != m - 1):
                   dp[j] = grid[i][j] + min(dp[j], dp[j + 1]);
               else:
                   dp[j] = grid[i][j];                
        return dp[0]


def main():
    grid = [[1,3,1],[1,5,1],[4,2,1]]       # expect is 7
    obj = Solution()
    result = obj.minPathSum(grid)
    print("return result is :",result)
    
if __name__ =='__main__':
    main()    