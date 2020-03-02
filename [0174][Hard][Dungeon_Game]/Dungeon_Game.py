# -*- coding: utf-8 -*-  
# leetcode time     cost : 56 ms
# leetcode memory   cost : 14.2 MB
# solution 1, DP
class Solution:
    def calculateMinimumHP(self, dungeon):
        m = len(dungeon)
        n = len(dungeon[0])
        
        dp = [[0 for i in range(n+1)] for i in range(m+1)]
        dp[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1])
        for i in range(m-2,-1,-1):
            dp[i][n-1] = max(1, dp[i+1][n-1] - dungeon[i][n-1])
        
        for i in range(n-2,-1,-1):
            dp[m-1][i] = max(1, dp[m-1][i+1] - dungeon[m-1][i])
        

        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                dpmin = min(dp[i+1][j], dp[i][j+1])
                dp[i][j] = max(1, dpmin - dungeon[i][j])

        return dp[0][0]


def main():
    dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]            #expect is 7
    obj = Solution()
    result = obj.calculateMinimumHP(dungeon)
    assert result == 7, ["hint: result is wrong"]
    print("return result is :",result)
    
if __name__ =='__main__':
    main()