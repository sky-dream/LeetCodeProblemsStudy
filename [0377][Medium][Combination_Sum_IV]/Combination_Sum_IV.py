# solution 1, analysis.
# leetcode time     cost : 48 ms
# leetcode memory   cost : 13.9 MB 
# Time  Complexity: O(N)
# Space Complexity: O(N)
# solution 1,DP, refer to No.518
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        dp = [0] * (target+1)
        dp[0] = 1
        for i in range(1,target+1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i-num]
        return dp[target]