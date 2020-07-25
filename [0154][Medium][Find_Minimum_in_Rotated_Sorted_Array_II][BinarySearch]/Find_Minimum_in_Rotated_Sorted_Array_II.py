# -*- coding: utf-8 -*-  
# leetcode time     cost : 48 ms
# leetcode memory   cost : 13.9 MB
# Time  Complexity: O(logN)
# Space Complexity: O(1)
# solution 1, binary search
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:    
        low, high = 0, len(nums) - 1
        while low < high:
            pivot = low + (high - low) // 2
            if nums[pivot] < nums[high]:
                high = pivot 
            elif nums[pivot] > nums[high]:
                low = pivot + 1
            else:
                high -= 1
        return nums[low]

def main():
    nums = [2,2,2,0,1]        #expect is 0
    obj = Solution()
    result = obj.findMin(nums)
    print("return result is :",result)
    
if __name__ =='__main__':
    main()   