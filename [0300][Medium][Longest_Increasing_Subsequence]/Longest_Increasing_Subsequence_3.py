# leetcode time     cost : 84 ms
# leetcode memory   cost : 13.8 MB 
# Time  Complexity: O(n**2)
# Space Complexity: O(n)
# slolution 3, DP,
class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums:  return 0
        best = [nums[0]]
        for i in range(1, len(nums)):
            index = self.upperBound(best, nums[i], 0, len(best))
            if index == len(best): best.append(nums[i])
            else: best[index] = nums[i]
        return len(best)

    # Return smallest index i such that array[i] >= target
    # or return end+1 if none (target > all array elements)
    def upperBound(self, array, target, start, end):
        if start >= end: return start
        m = (end+start)//2
        if array[m] >= target:
            if m == start or array[m-1] < target: return m
            return self.upperBound(array, target, start, m)
        return self.upperBound(array, target, m+1, end)