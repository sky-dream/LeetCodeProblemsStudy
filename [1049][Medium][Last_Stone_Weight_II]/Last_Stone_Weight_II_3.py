# leetcode time     cost : 52 ms
# leetcode memory   cost : 13.8 MB 
# Time  Complexity: O(N*sum)
# Space Complexity: O(N)
# solution 1, DP, refer to 494, add +,- for num in nums to get a target
# 可以变成 选出一些数字，使得它们最逼近整个数组和除以二的值，而最后的结果，就是abs（这个数-总和除以二）*2
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total, l = sum(stones), len(stones)
        dp = [[0]*(total//2+1) for _ in range(l+1)]
        for i in range(1, l+1):
            for j in range(1, total//2+1):
                if stones[i-1]<=j: # 这个代表选第i个, 然后再去比较选之后的大小
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-stones[i-1]]+stones[i-1])
                else: dp[i][j] = dp[i-1][j] # 这个代表不选第i个
        return total-2*dp[-1][-1]
    
    def lastStoneWeightII_2(self, stones: List[int]) -> int:
        total, l = sum(stones), len(stones)
        dp = [0]*(total//2+1)
        for i in range(0, l): # 因为没有了i-1所以可以从0开始
            for j in range(total//2, stones[i]-1, -1):
                    dp[j] = max(dp[j], dp[j-stones[i]]+stones[i])
        return total-2*dp[-1]