# leetcode time     cost : 1692 ms
# leetcode memory   cost : 38.3 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
# solution 1 DP,
class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        n = len(prob)
        # dp[i][j], i is the i th prob[i], j is the num of coin facing heads
        dp = [[0 for _ in range(n+1)] for _ in range(n)]
        # set init value when touch prob[0]
        dp[0][0], dp[0][1] = 1- prob[0], prob[0]
        for i in range(1, n):
            for j in range(0, min(i+2, target+1)):
                dp[i][j] = (1-prob[i]) * dp[i-1][j] + prob[i] * dp[i-1][j-1]
        return dp[n-1][target]