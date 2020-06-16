# leetcode time     cost : 40 ms
# leetcode memory   cost : 13.1 MB 
# solution 1, loop twice
# Time  Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)-1
        i = n-1
        # start from right,find the num need increase
        while (i >= 0) and (nums[i] >= nums[i+1]):
            i-=1
        if (i >= 0):
            j = n
            # start from right,find the num new value
            while (j >= 0 and nums[j] <= nums[i]):
                j-=1
            nums[i], nums[j] = nums[j], nums[i]
        # reverse the decending right part to get its smalest value 
        # a=[1,2,3,4,5,6,7,8,9], a[2:5]=a[5-1:2-1:-1],[1, 2, 5, 4, 3, 6, 7, 8, 9]  
        nums[i+1:] = list(reversed(nums[i+1:]))