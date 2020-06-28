# -*- coding: utf-8 -*- 
# leetcode time     cost : 56 ms
# leetcode memory   cost : 14.7 MB
# solution 3, bit xor
# Time  Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
    
    
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