# leetcode time     cost : 40 ms
# leetcode memory   cost : 13.7 MB 
# Time  Complexity: O(N*logN)
# Space Complexity: O(n)
# slolution 3, DP,
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1] * len(nums)
        ans = 0
        for i,num in enumerate(nums):
            ans =max(ans,dp[i])
            for j in range(i+1,len(nums)):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j],dp[i]+1)
        return ans
    
    # solution 4,DP and binarySearch,
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []
        for num in nums:
            bi = bisect.bisect_left(dp,num)
            if bi == len(dp):
                dp += num,
            else:
                dp[bi] = num
        return len(dp)