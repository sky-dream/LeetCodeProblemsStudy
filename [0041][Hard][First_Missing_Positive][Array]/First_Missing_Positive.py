# leetcode time     cost : 48 ms
# leetcode memory   cost : 13.6 MB
# Time  Complexity: O(N)
# Space Complexity: O(1)
# solution 1, hash table with set flag for included elements position
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # update all none positive integer
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        # set flag for position if related num exists
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])
        # search position with no flags
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        
        return n + 1