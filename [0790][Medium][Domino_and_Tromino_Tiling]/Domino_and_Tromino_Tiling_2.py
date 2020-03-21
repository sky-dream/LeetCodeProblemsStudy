# leetcode time     cost : 48 ms
# leetcode memory   cost : 13.5 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
# solution 1, DP
class Solution(object):
    def numTilings(self, N):
        MOD = 10**9 + 7
        # dp[i][0] both rows are covered for column i,
        # dp[i][1] up row is covered  for column i,
        # dp[i][2] up row is covered  for column i, dp[i][1] == dp[i][2]
        dp = [[0]*3 for _ in range(N+1)]
        # init dp, 
        dp[0][0] = dp[1][0] = 1
        for i in range(2,N+1):
            dp[i][0] = (dp[i-1][0] + dp[i-2][0] + dp[i-1][1] +dp[i-1][2]) % MOD
            dp[i][1] = (dp[i-2][0] + dp[i-1][2]) % MOD
            dp[i][2] = (dp[i-2][0] + dp[i-1][1]) % MOD

        return dp[N][0]

def main():
    n = 3      #expect is 5
    obj = Solution()
    res = obj.numTilings(n)
    print("return value is ",res);
    
if __name__ =='__main__':
    main()   