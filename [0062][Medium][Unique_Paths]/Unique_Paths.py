# -*- coding: utf-8 -*-  
# leetcode time     cost : 40 ms
# leetcode memory   cost : 13.5 MB
# Time  Complexity: O(m*n)
# Space Complexity: O(m*n)
# solution 1 DP
class Solution:
    #def uniquePaths(self, m: int, n: int) -> int:
    def uniquePaths(self, m, n):    # m is column number, n is the row number 
        # the first col and first row should be init as 1. 
        dp = [ [1]*n ] + [  [1]+[0] * (n-1) for _ in range(m-1)  ]
        #print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

def main():
    m,n = 7,3       # expect is 28
    obj = Solution()
    result = obj.uniquePaths(m,n)
    print("return result is :",result)
    
if __name__ =='__main__':
    main()   