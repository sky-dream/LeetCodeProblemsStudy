# leetcode time     cost : 28 ms
# leetcode memory   cost : 13.5 MB 
# Time  Complexity: O(n)
# Space Complexity: O(1)
# solution 1,DP, refer to leetcode 198, House_Robber, 0_1 problem
class Solution:
    def massage(self, nums: [int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        dp0, dp1 = 0, nums[0]
        for i in range(1, n):
            tdp0 = max(dp0, dp1)   # 计算 dp[i][0]
            tdp1 = dp0 + nums[i]   # 计算 dp[i][1]
            dp0, dp1 = tdp0, tdp1
        
        return max(dp0, dp1)

def main():
    nums = [2,7,9,3,1]            #expect is 12
    obj = Solution()
    result = obj.massage(nums)
    print("return result is :",result)
    
if __name__ =='__main__':
    main()   