# -*- coding: utf-8 -*-  
# leetcode time     cost : 60 ms
# leetcode memory   cost : 15.1 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True      # 如果只有一个元素则一定可以到达
        max_distance = 0                    # 设定可以达到的最大坐标
        for i in range(len(nums)):
            if i > max_distance:            # 表示当前坐标无法跳跃达到
                return False
            max_distance = max(max_distance, i + nums[i])  # 更新可以达到的最远坐标
        return True  
    
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