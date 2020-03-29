# leetcode time     cost : 236 ms
# leetcode memory   cost : 19.2 MB 
# Time  Complexity: O(m*n*N)
# Space Complexity: O(m*n)
# solution 1, DP,refer to No.688
class Solution(object):
    def findPaths(self, m, n, N, i, j):
        # 增加网格边界，初始值设为1。 dp[k][row][col]表示网格在(row-1, col-1)位置时，经过N此移动出边界的次数
        dp = [[[0 for col in range(n+2)] for row in range(m+2)] for k in range(N+1)]
        for k in range(N+1):
            for row in range(m+2):
                for col in range(n+2):
                    if row == 0 or row == m+1 or col == 0 or col == n+1:
                        dp[k][row][col] = 1
        
        for k in range(1, N+1):
            for row in range(1, m+1):
                for col in range(1, n+1):
                    dp[k][row][col] = dp[k-1][row-1][col] + dp[k-1][row+1][col] + dp[k-1][row][col-1] + dp[k-1][row][col+1]
        # 位置(i,j)移动k 次出边界，== 所有可能导致出边界的点 在 k 次移动中 到达 位置（i,j）的总次数
        return dp[N][i+1][j+1] % (10**9 + 7)
    
def main():
    m, n, N, i, j = 1,3,1,0,1  # ans 2
    obj = Solution()
    res = obj.findPaths(m, n, N, i, j)
    print("return value is ",res)
    
if __name__ =='__main__':
    main()     