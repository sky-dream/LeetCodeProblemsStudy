# -*- coding: utf-8 -*-  
# leetcode time     cost : 40 ms
# leetcode memory   cost : 13.7 MB
# Time  Complexity: O(logN)
# Space Complexity: O(1)
# solution 1, binary search
class Solution:
    def findMin(self, nums) -> int:
        n = len(nums)
        l,r = 0,n-1
        res = nums[0]
        # terminate if only 2 elements left, l+1==r,
        while l<r:    
            mid = l + (r-l)//2
            # min value is just after the max value in the middle
            if nums[mid] > nums[mid + 1]:
                res = min(res,nums[mid + 1])
            if nums[l] < nums[mid] and nums[mid] > nums[r]:  # left part is ascending order but right side not, min value is in right side
                l = mid
                res = min(res,nums[mid + 1])
            elif nums[mid] < nums[r] and nums[l] > nums[mid]:  # right part is ascending order but left side not, min value is in left side
                r = mid
                res = min(res,nums[mid])
            else: # all part in ascending order,[1,2], [1,2,3]
                r = mid                                                                
                res = min(res,nums[l])  
        return res

def main():
    nums = [4,5,6,7,0,1,2]        #expect is 0
    obj = Solution()
    result = obj.findMin(nums)
    print("return result is :",result)
    
if __name__ =='__main__':
    main()   