# -*- coding: utf-8 -*-  
# leetcode time     cost : 48 ms
# leetcode memory   cost : 13.8 MB
# Time  Complexity: O(N*log(array_sum))
# Space Complexity: O(1)
# solution 1, binary search
# 答案必然在max(nums),sum(nums)区间，不断尝试不同的答案，
# 检验符合该答案时，子数组的分解个数和目标子数组个数m的关系
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left, right = max(nums),sum(nums)
        while left < right:
            mid = (left + right) // 2
            sums, cnt = 0, 1
            for i in nums:
                if sums + i > mid:
                    cnt += 1
                    sums = i
                else:
                    sums += i
            if cnt <= m:
                right = mid
            else:
                left = mid + 1
        return left