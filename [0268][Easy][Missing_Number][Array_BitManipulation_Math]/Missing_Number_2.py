# -*- coding: utf-8 -*- 
# leetcode time     cost : 32 ms
# leetcode memory   cost : 15.2 MB
# solution 2, hash set
# Time  Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def missingNumber(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number
    
    
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