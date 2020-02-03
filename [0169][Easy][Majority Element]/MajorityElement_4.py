#solution 4, random choice function,
# leetcode time     cost : 168 ms
# leetcode memory   cost : 13.2 MB 
# Time  Complexity: O(∞)
# Space Complexity: O(1)
import random
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority_count = len(nums)//2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate