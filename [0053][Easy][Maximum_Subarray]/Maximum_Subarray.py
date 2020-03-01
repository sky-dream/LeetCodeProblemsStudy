# leetcode time     cost : 52 ms
# leetcode memory   cost : 14.5 MB 
# solution 1, DP
# Time  Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        # dp[i] is the max sub array that include current num[i] 
        dp = [0 for i in range(n)]
        max_sum = dp[0] = nums[0]
        for i in range(1,n):
            dp[i] = nums[i] + (dp[i-1] if dp[i-1] > 0 else 0)
            max_sum = max(max_sum, dp[i])
        return  max_sum   
    
def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4]          # [4,-1,2,1], expect is 6
    obj = Solution()
    result = obj.maxSubArray(nums)
    print("return result is :",result)
    
if __name__ =='__main__':
    main() 