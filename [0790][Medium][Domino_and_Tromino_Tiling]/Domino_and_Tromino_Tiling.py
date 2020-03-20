# leetcode time     cost : 36 ms
# leetcode memory   cost : 13.5 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
# solution 1, DP
class Solution(object):
    def numTilings(self, N):
        MOD = 10**9 + 7
        dp = [1, 0, 0, 0]
        for _ in range(N):
            ndp = [0, 0, 0, 0]
            ndp[0b00] = (dp[0b00] + dp[0b11]) % MOD
            ndp[0b01] = (dp[0b00] + dp[0b10]) % MOD
            ndp[0b10] = (dp[0b00] + dp[0b01]) % MOD
            ndp[0b11] = (dp[0b00] + dp[0b01] + dp[0b10]) % MOD
            dp = ndp

        return dp[0]

def main():
    n = 3      #expect is 5
    obj = Solution()
    res = obj.numTilings(n)
    print("return value is ",res);
    
if __name__ =='__main__':
    main()   