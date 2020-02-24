# leetcode time     cost : 1220 ms
# leetcode memory   cost : 13.8 MB 
# Time  Complexity: O(n*k)
# Space Complexity: O(n)
# slolution 3, DP
class Solution:
    #def lengthOfLIS(self, nums: List[int]) -> int:
    def lengthOfLIS(self, nums):    
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    
        return max(dp)
    
def main():
    nums = [1,3,6,7,9,4,10,5,6] #expect is 6
    obj = Solution()
    result = obj.lengthOfLIS(nums)
    print("return result is "+str(result));

if __name__ =='__main__':
    main() 