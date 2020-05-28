# -*- coding: utf-8 -*-
# solution 1,
# Time  Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # 循环记录0元素的个数，并且遇到非0元素时候，将非0元素替换到0元素的位置
        # count 记录0元素的个数， i - count实际上是记录了零元素的位置。
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            elif count > 0:
                nums[i - count], nums[i] = nums[i], 0
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