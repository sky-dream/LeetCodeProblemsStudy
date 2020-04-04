# leetcode time     cost : 1444 ms
# leetcode memory   cost : 13.7 MB 
# Time  Complexity: O(N*N*N)
# Space Complexity: O(N*N)
# solution 2,dp from bottom to top
# 2 dp process running at the same time
# https://leetcode-cn.com/problems/cherry-pickup/solution/zhai-ying-tao-by-leetcode/
class Solution(object):
    def cherryPickup(self, grid):
        N = len(grid)
        dp = [[float('-inf')] * N for _ in range(N)]
        dp[0][0] = grid[0][0]
        for t in range(1, 2*N - 1):
            dp2 = [[float('-inf')] * N for _ in range(N)]
            for i in range(max(0, t-(N-1)), min(N-1, t) + 1):
                for j in range(max(0, t-(N-1)), min(N-1, t) + 1):
                    if grid[i][t-i] == -1 or grid[j][t-j] == -1:
                        continue
                    val = grid[i][t-i]
                    if i != j: val += grid[j][t-j]
                    dp2[i][j] = max(dp[pi][pj] + val
                                    for pi in (i-1, i) for pj in (j-1, j)
                                    if pi >= 0 and pj >= 0)
            dp = dp2
        return max(0, dp[N-1][N-1])


def main():
    grid = [[0,1,-1],[1,0,-1],[1,1,1]]    #expect is 5
    obj = Solution()
    result = obj.cherryPickup(grid)
    print("return result is ",result);

if __name__ =='__main__':
    main() 