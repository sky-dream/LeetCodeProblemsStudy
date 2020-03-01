# -*- coding: utf-8 -*-  
# leetcode time     cost : 40 ms
# leetcode memory   cost : 13.5 MB
# Time  Complexity: O(m*n)
# Space Complexity: O(1)
# solution 1 DP
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # If the starting cell has an obstacle, then simply return as there would be
        # no paths to the destination.
        if obstacleGrid[0][0] == 1:
            return 0

        # init dp, dp[i][j] is the paths value when come to obstacleGrid[i][j]
        dp = [[0 for i in range(n)] for i in range(m)]
        
        # Number of ways of reaching the starting cell = 1.
        obstacleGrid[0][0] = dp[0][0] =1

        # Filling the values for the first column
        for i in range(1,m):
            dp[i][0] = int(obstacleGrid[i][0] == 0 and dp[i-1][0] == 1)

        # Filling the values for the first row        
        for j in range(1, n):
            dp[0][j] = int(obstacleGrid[0][j] == 0 and dp[0][j-1] == 1)

        # Starting from cell(1,1) fill up the values
        # No. of ways of reaching cell[i][j] = cell[i - 1][j] + cell[i][j - 1]
        # i.e. From above and left.
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0

        # Return paths value dp[m-1][n-1] when come to rightmost bottommost cell. That is the destination.            
        return dp[m-1][n-1]

def main():
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]       # expect is 2
    obj = Solution()
    result = obj.uniquePathsWithObstacles(obstacleGrid)
    print("return result is :",result)
    
if __name__ =='__main__':
    main()   