# leetcode time     cost : 40 ms
# leetcode memory   cost : 13.6 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
# 2 diferent DP expressions,
class Solution:
  def rob(self, nums):
    # Base Case: nums[0] = nums[0]
    # nums[1] = max(nums[0], nums[1])
    # nums[k] = max(k + nums[k-2], nums[k-1])
    '''
    # Approach 1:- Construct dp table
    if not nums: return 0
    if len(nums) == 1: return nums[0]
    
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
      dp[i] = max(nums[i] + dp[i-2], dp[i-1])
    return dp[-1] # return the last element
    '''
    
    # Approach 2:- Constant space use two variables and compute the max respectively
    prev = curr = 0
    for num in nums:
      temp = prev # This represents the nums[i-2]th value
      prev = curr # This represents the nums[i-1]th value
      curr = max(num + temp, prev) # Here we just plug into the formula
    return curr

def main():
    array = [2,3,2]      #expect is 3   
    obj = Solution()
    res = obj.rob(array)
    print("return value is ",res);
    
if __name__ =='__main__':
    main() 