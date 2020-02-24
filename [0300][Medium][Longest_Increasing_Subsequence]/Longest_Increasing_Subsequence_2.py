# leetcode time     cost : 52 ms
# leetcode memory   cost : 13.9 MB 
# Time  Complexity: O(N*logN)
# Space Complexity: O(N)
# slolution 4, DP and binarySearch with bisect lib,
import bisect
class Solution:
    #def lengthOfLIS(self, nums: List[int]) -> int:
    def lengthOfLIS(self, nums):
        # minend[i] is the minimum ending of an increasing subsequence of length i+1.
        minend = [float('inf')] * (len(nums) + 1)
        for num in nums:
            minend[bisect.bisect_left(minend, num)] = num
        return minend.index(float('inf'))
    
    def lengthOfLIS_2(self, nums):
        minend = [float('inf')] * len(nums)
        for num in nums:
            minend[bisect.bisect_left(minend, num)] = num
        return bisect.bisect_left(minend, float('inf'))