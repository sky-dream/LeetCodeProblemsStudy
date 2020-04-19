# -*- coding: utf-8 -*-  
# leetcode time     cost : 80 ms
# leetcode memory   cost : 15.1 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(ans, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans
    
def main():
    height = [1,8,6,2,5,4,8,3,7]
    expect = 49
    obj = Solution()
    result = obj.maxArea(height)
    try:
        assert result == expect
        print("passed, result is follow expect:",result)
    except AssertionError as aError:
        print('failed, result is wrong', result, aError.__str__())
    
if __name__ =='__main__':
    main()  