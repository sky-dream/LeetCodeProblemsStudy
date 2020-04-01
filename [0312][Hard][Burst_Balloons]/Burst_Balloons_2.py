# leetcode time     cost : 564 ms
# leetcode memory   cost : 14 MB 
# Time  Complexity: O(N*N*N)
# Space Complexity: O(N*N)
# SOLUTION 1, DP, from Bottom to Top
class Solution:
    def maxCoins(self, nums: [int]) -> int:

        # reframe problem as before
        nums = [1] + nums + [1]
        n = len(nums)

        # dp will store the results of our calls
        dp = [[0] * n for _ in range(n)]

        # iterate over dp and incrementally build up to dp[0][n-1]
        for left in range(n-2, -1, -1):
            for right in range(left+2, n):
                # same formula to get the best score from (left, right) as before
                for i in range(left+1, right):
                    dp[left][right] = max(dp[left][right],nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])

        return dp[0][n-1]
    
def main():
    nums = [3,1,5,8]         #expect is 167
    s = Solution()
    res = s.maxCoins(nums) 
    print("in python,res is : ",res)
if __name__ =='__main__':
    main()    