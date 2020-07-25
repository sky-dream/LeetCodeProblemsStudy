# leetcode time     cost : 52 ms
# leetcode memory   cost : 13.8 MB 
# solution 2, # binary Search with recursion
# Time  Complexity: O(logN)
# Space Complexity: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        def binarySearch(nums,lo,hi,target,level):
            #print("level: ",level,",lo: ",lo,",hi: ",hi)
            if lo>hi:
                return -1
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    return binarySearch(nums,lo,mid-1,target,level+1)
                    
                else:
                    return binarySearch(nums,mid+1,hi,target,level+1)
                    
            else:
                if nums[mid] < target <= nums[hi]:
                    return binarySearch(nums,mid+1,hi,target,level+1)
                else:
                    return binarySearch(nums,lo,mid-1,target,level+1)
        l, r = 0, len(nums) - 1
        res = binarySearch(nums,l,r,target,0)
        return res