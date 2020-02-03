#solution 3, sort,
# leetcode time     cost : 152 ms
# leetcode memory   cost : 13.2 MB 
# Time  Complexity: O(nlgn)
# Space Complexity: O(1) or O(N)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)//2]