# solution 1, brute force calculation,
# leetcode time     cost : na ms
# leetcode memory   cost : na MB 
# Time  Complexity: O(N*N)
# Space Complexity: O(1)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority_count = len(nums)//2
        for num in nums:
            count = sum(1 for elem in nums if elem == num)
            if count > majority_count:
                return num