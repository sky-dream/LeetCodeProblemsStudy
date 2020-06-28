#-*- coding: utf-8 -*-  
# leetcode time     cost : 104 ms
# leetcode memory   cost : 16 MB
# solution 3, 2 pointers, fast and slow pointers
# Time  Complexity: O(N)
# Space Complexity: O(1)
# https://leetcode-cn.com/problems/find-the-duplicate-number/solution/kuai-man-zhi-zhen-de-jie-shi-cong-damien_undoxie-d/
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        slow = nums[slow]
        fast = nums[nums[fast]]
        while (slow != fast):
            slow = nums[slow]
            fast = nums[nums[fast]]
        finder = 0
        while (finder != slow):
            finder = nums[finder]
            slow = nums[slow]
        return slow