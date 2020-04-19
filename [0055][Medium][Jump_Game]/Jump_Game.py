# -*- coding: utf-8 -*-  
# leetcode time     cost : 60 ms
# leetcode memory   cost : 15.2 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False 
    
def main():
    nums = [2,3,1,1,4]
    expect = True
    obj = Solution()
    result = obj.canJump(nums)
    try:
        assert result == expect
        print("passed, result is follow expect:",result)
    except AssertionError as aError:
        print('failed, result is wrong', result, aError.__str__())
    
if __name__ =='__main__':
    main()  