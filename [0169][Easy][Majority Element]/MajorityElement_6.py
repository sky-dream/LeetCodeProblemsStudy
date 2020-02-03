# solution 6，Boyer-Moore votes，
# leetcode time     cost : 156 ms
# leetcode memory   cost : 13.4 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate 