# solution 2, DP.
# leetcode time     cost : 36 ms
# leetcode memory   cost : 13.2 MB 
# Time  Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        dp[1] = 1
        for i in range(n+1):		
            for j in range(i):	
                dp[i] = max(dp[i], max(dp[j],j) * (i - j))
        return dp[n]