# -*- coding: utf-8 -*-  
# leetcode time cost : 1012 ms
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(0,len(nums)):
            if i >0 and nums[i] == nums [i-1]:
                continue
            target = 0 - nums[i]
            start,end = i+1, len(nums) - 1
            while start < end:
                if nums[start] + nums[end] > target:
                    end = end-1
                elif nums[start] + nums[end] < target:
                    start = start + 1
                else:
                    res.append((nums[i],nums[start],nums[end]))
                    end = end -1
                    start = start +1
                    while start < end and nums[end] == nums[end+1]:
                        end = end - 1
                    while start < end and nums[start] == nums[start-1]:
                        start = start + 1
        return res