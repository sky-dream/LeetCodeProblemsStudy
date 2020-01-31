# -*- coding: utf-8 -*-  
# leetcode time cost : 1064 ms
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []

        if all(num == 0 for num in nums):
            return [[0,0,0]]
        
        found = set(tuple())        #initialize found = set(tuple())
        nums = sorted(nums)
        rightmost = len(nums)-1
        
        #Fix the first element, then search for the other two
        for index, eachNum in enumerate(nums):
            left = index + 1 
            right = rightmost
            
            while left < right: 
                check_sum = (eachNum + nums[left] + nums[right])                
        #Since the list is sorted, we can check whether the leftmost or the rightmost element is causing the sum!=0 
                if check_sum == 0:
                    new_found = (eachNum, nums[left], nums[right])      
                    #use add not append for the tuple(), then no need to check duplicate if new_found not in found: 
                    found.add(new_found)        
        #even if we find the element, we need to decrease right, to find all other pairings with the first number
                    right -=1                    
        #if the sum is less than 0, then our 2nd number is too low, we check the next highest one in our sorted list
                elif check_sum < 0: 
                    left += 1                
        #if the sum is less than 0, then our 3rd number is too high, we check the next lowest one in our sorted list
                else: 
                    right -= 1        
        return found   