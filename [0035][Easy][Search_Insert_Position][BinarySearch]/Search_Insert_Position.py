# Time  Complexity: O(logN)
# Space Complexity: O(1)
# solution 1, binary search
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        start,end = 0,len(nums)-1
        while(start<=end):
            mid = start + (end-start)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                start = mid+1
            else:
                end = mid-1
        return start