# leetcode time     cost : 48 ms
# leetcode memory   cost : 14.2 MB 
# solution 3, greedy
# Time  Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        curr_sum = max_sum = nums[0]

        for i in range(1, n):
            # exclude the sum before if curr_sum based on before elements is negative
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)
            
        return max_sum
    
def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4]          # [4,-1,2,1], expect is 6
    obj = Solution()
    result = obj.maxSubArray(nums)
    print("return result is :",result)
    
if __name__ =='__main__':
    main() 