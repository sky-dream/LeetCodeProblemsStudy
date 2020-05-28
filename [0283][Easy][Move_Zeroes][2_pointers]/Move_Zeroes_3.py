# -*- coding: utf-8 -*-
# solution 3,
# Time  Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 循环遍历数组，当遇到非零元素的时候替换掉前面0元素
        # j 记录最新非零元素的位置
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                if i != j:
                    nums[i] = 0
                j += 1
        return nums
def main():
    inputX,expectRes = [0,1,0,3,12],[1,3,12,0,0]
    obj = Solution()
    result = obj.moveZeroes(inputX)
    try:
        assert result == expectRes
        print("passed, result is follow expect:",result)
    except AssertionError as aError:
        print('failed, result >> ', result,"<< is wrong, ","expect is : "+ expectRes)
    
if __name__ =='__main__':
    main() 