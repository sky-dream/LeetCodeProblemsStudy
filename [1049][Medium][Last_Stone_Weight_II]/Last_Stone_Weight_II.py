# leetcode time     cost : 80 ms
# leetcode memory   cost : 13.9 MB 
# Time  Complexity: O(N*sum)
# Space Complexity: O(N)
# solution 1, DP, refer to 0-1 knapack
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # dp[i][j] , all the left rocks min weight sum, 
        # i is the status nums[0:i], j is the max weight stones that destroyed.
        # when come to end, if get 0, then j_max == sum(stones)//2
        # stones[i] has 2 status, keep, destroy by combine with others
        n = len(stones)
        max_destroy = sum(stones)//2+1
        dp = [[0]*(max_destroy) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(max_destroy):
                if stones[i-1]<=j:
                    dp[i][j] = max(dp[i-1][j],dp[i-1][j-stones[i-1]]+stones[i-1])
                else:
                    dp[i][j] = dp[i-1][j] 
        # remove 2 times of all the destroyed weight
        return sum(stones) - 2* dp[n][max_destroy-1]