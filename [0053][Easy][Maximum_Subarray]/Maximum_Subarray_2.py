# leetcode time     cost : 260 ms
# leetcode memory   cost : 14.3 MB 
# solution 2, divide and conquer approach
# Time  Complexity: O(NlogN)
# Space Complexity: O(logN)
class Solution:
    def cross_sum(self, nums, left, right, mid): 
            if left == right:
                return nums[left]

            left_subsum = float('-inf')
            curr_sum = 0
            # scan from right to left for left part array
            for i in range(mid, left - 1, -1):
                curr_sum += nums[i]
                left_subsum = max(left_subsum, curr_sum)

            right_subsum = float('-inf')
            curr_sum = 0
            for i in range(mid + 1, right + 1):
                curr_sum += nums[i]
                right_subsum = max(right_subsum, curr_sum)

            return left_subsum + right_subsum   
    
    def helper(self, nums, left, right): 
        if left == right:
            return nums[left]
        
        mid = (left + right) // 2
            
        left_sum = self.helper(nums, left, mid)
        right_sum = self.helper(nums, mid + 1, right)
        cross_sum = self.cross_sum(nums, left, right, mid)
        
        return max(left_sum, right_sum, cross_sum)
        
    def maxSubArray(self, nums):
        return self.helper(nums, 0, len(nums) - 1)
    
def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4]          # [4,-1,2,1], expect is 6
    obj = Solution()
    result = obj.maxSubArray(nums)
    print("return result is :",result)
    
if __name__ =='__main__':
    main() 