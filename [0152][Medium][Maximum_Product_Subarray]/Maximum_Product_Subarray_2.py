# -*- coding: utf-8 -*-  
# leetcode time     cost : 44 ms
# leetcode memory   cost : 13.7 MB
# solution 1, DP by scan forward and backward.
class Solution(object):
    def maxProduct(self, nums):
        res = -float('inf')
        product = 1
        length = len(nums)
        for i in range(length):
            product *= nums[i]
            res = max(product, res)
            if nums[i] == 0:
                product = 1
        # scan backward
        product = 1
        for j in range(length - 1, -1, -1):
            product *= nums[j]
            res = max(product, res)
            if nums[j] == 0:
                product = 1
        return res

def main():
    nums = [2,3,-2,4]        #expect is 6
    obj = Solution()
    result = obj.maxProduct(nums)
    print("return result is :",result)
    
if __name__ =='__main__':
    main()   