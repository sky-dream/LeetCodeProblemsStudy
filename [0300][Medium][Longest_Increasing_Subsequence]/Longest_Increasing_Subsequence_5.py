# leetcode time     cost : 52 ms
# leetcode memory   cost : 13.7 MB 
# Time  Complexity: O(n)
# Space Complexity: O(n)
# solution 4,DP and binarySearch,
class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums: return 0
        res = [nums[0]]
        for num in nums:
            if num <= res[0]: res[0] = num
            elif num > res[-1]: res.append(num)
            else:
                indx = self.binarysearch(res, 0, len(res), num)
                res[indx] = num   # in insertion sort you use insert(), here you simply replace it
        return len(res)

    def binarysearch(self, nums, l, r, target):
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target: l = mid + 1
            else: r = mid
        return l
    
    # solution 4,DP and binarySearch with bisect lib,
    def lengthOfLIS(self, nums):
        if not nums: return 0
        res = []
        for num in nums:
            indx = bisect.bisect_left(res, num)
            if indx == len(res): res.append(num)
            else: res[indx] = num
        return len(res)