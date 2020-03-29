# leetcode time     cost : 532 ms
# leetcode memory   cost : 13.5 MB 
# Time  Complexity: O(m*n*N)
# Space Complexity: O(m*n)
# solution 1, DP,refer to No.688
class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        dp = dp2 = [[0]*n for _ in range(m)]
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        max_divider = 10**9+7
        dp[i][j] = 1        # init the start point
        res = 0
        if N ==0:
            return 0
        if m==1 and n==1:
            return 4
        def isOutOfBound(row,col):
            return not (0<=row<m and 0<=col<n)
        for k in range(N):
            dp2 = [[0]*n for _ in range(m)]
            for row in range(m):
                for col in range(n):
                    for direct in directions:
                        new_row = row + direct[0]
                        new_col = col + direct[1]
                        if isOutOfBound(new_row,new_col):
                            res = (res + dp[row][col]) % max_divider
                        else:
                            dp2[new_row][new_col] += (dp[row][col])% max_divider
            dp = dp2
        return res
    
def main():
    m, n, N, i, j = 1,3,1,0,1  # ans 2
    obj = Solution()
    res = obj.findPaths(m, n, N, i, j)
    print("return value is ",res)
    
if __name__ =='__main__':
    main()     