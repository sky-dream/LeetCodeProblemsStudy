# -*- coding: utf-8 -*-  
# leetcode time     cost : 44 ms
# leetcode memory   cost : 13.6 MB
# Time  Complexity: O(logN)
# Space Complexity: O(1)
# solution 1, binary search
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 or nums[0]<nums[n-1]:
            return nums[0]
        l,r = 0,n-1
        # terminate if l > r,
        while l <= r:    
            mid = l + (r-l)//2
            # if the mid element is greater than its next element then mid+1 element is the smallest
            # This point would be the point of change. From higher to lower value.
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            # if the mid element is lesser than its previous element then mid element is the smallest
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
                
            # if the mid elements value is greater than the 0th element this means
            # the least value is still somewhere to the right as we are still dealing with elements greater than nums[0]
            if nums[mid] > nums[0]:
                l = mid + 1
            # if nums[0] is greater than the mid value then this means the smallest value is somewhere to the left
            else:
                r = mid - 1

def main():
    nums = [4,5,6,7,0,1,2]        #expect is 0
    obj = Solution()
    result = obj.findMin(nums)
    print("return result is :",result)
    
if __name__ =='__main__':
    main()   