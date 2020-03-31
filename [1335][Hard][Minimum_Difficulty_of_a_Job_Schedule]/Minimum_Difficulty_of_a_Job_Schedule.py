# leetcode time     cost : 7596 ms
# leetcode memory   cost : 13.9 MB 
# Time  Complexity: O(N*N *d)
# Space Complexity: O(N*d)
# solution 1,DP, refer to 813,1278
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        # dp[i][j] the min job schedule difficulty when 0 to i-th element is divided into j day
        dp = [[1000*300]*(d+1) for _ in range(n+1)]
        # set init value
        dp[0][0] = dp[0][1] = dp[1][0] = 0
        dp[1][1] = jobDifficulty[0]
        for i in range(1, n + 1):
            for j in range(1, min(d, i) + 1):
                if j == 1:
                    dp[i][j] = max(jobDifficulty[0:i])
                else:
                    for i0 in range(j - 1, i):
                        dp[i][j] = min(dp[i][j], dp[i0][j - 1] + max(jobDifficulty[i0:i]))
        return  dp[n][d] if dp[n][d] is not 300000 else -1