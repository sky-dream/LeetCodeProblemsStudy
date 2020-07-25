# -*- coding: utf-8 -*-  
# solution 1, 2 pointers
# Time  Complexity: O(N)
# Space Complexity: O(1)
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr,p0,p2 = 0, 0, (len(nums)-1)
        while (curr <= p2):
            if nums[curr] == 0:
                nums[p0],nums[curr] = nums[curr], nums[p0]
                curr+=1
                p0+= 1
            elif nums[curr] == 2:
                nums[p2],nums[curr] = nums[curr], nums[p2]
                p2-=1
            else:
                curr+=1

def main():
    nums = [2,0,2,1,1,0]
    obj = Solution()
    obj.sortColors(nums)
    assert nums == [0,0,1,1,2,2], ["hint: result is wrong"]
    print("return result is :",nums)
    
if __name__ =='__main__':
    main()   