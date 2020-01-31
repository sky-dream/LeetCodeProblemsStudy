# -*- coding: utf-8 -*-  
# leetcode time cost : 2456 ms
class Solution(object):
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums)-1
            
            while left < right:
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
        
        return list(res)   