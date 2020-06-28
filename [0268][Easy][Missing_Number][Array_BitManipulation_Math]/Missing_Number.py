# -*- coding: utf-8 -*- 
# leetcode time     cost : 64 ms
# leetcode memory   cost : 14.7 MB
# solution 1, sorting
# Time  Complexity: O(N*logN)
# Space Complexity: O(1)
class Solution:
    def missingNumber(self, nums):
        nums.sort()

        # Ensure that n is at the last index
        if nums[-1] != len(nums):
            return len(nums)
        # Ensure that 0 is at the first index
        elif nums[0] != 0:
            return 0

        # If we get here, then the missing number is on the range (0, n)
        for i in range(1, len(nums)):
            expected_num = nums[i-1] + 1
            if nums[i] != expected_num:
                return expected_num
    
    
def main():
    inputX,expectRes = [3,0,1], 2
    obj = Solution()
    result = obj.missingNumber(inputX)
    try:
        assert result == expectRes
        print("passed, result is follow expect:",result)
    except AssertionError as aError:
        print('failed, result >> ', result,"<< is wrong, ","expect is : "+ expectRes)
    
if __name__ =='__main__':
    main() 