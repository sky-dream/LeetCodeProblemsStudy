# leetcode time     cost : 2000 ms
# leetcode memory   cost : 17.4 MB 
# Time  Complexity: O(N*sum)
# Space Complexity: O(N*sum)
# solution 1,DP, refer to No.518
class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #背包问题+动态规划
        target=sum(nums)
        if target%2==1:return False
        target=target//2
        n=len(nums)
        dp=[[False]*(target+1) for _ in range(n)]

        for k in range(target+1):
            if nums[0]==k:
                dp[0][k]=True
                break

        for i in range(1,n):
            for j in range(1,target+1):
                if j >=nums[i]:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-nums[i]]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[-1][-1]