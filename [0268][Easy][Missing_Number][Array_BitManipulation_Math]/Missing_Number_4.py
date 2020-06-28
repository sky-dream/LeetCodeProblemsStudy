# -*- coding: utf-8 -*- 
# leetcode time     cost : 48 ms
# leetcode memory   cost : 14.6 MB
# solution 4, math, sum the nums, sum value maybe overflow
# Time  Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def missingNumber(self, nums):
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
    
    
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