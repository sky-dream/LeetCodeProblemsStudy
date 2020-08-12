# -*- coding: utf-8 -*-  
# Time  Complexity: O(n)
# Space Complexity: O(1)
# solution 1, 2 pointers
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        i = 0 
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1