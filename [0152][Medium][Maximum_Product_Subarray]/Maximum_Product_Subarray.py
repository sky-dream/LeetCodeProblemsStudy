# -*- coding: utf-8 -*-  
# leetcode time     cost : 52 ms
# leetcode memory   cost : 13.6 MB
# solution 1, DP, Save Min value and Max value at each node and the result works out.
class Solution:
    #def maxProduct(self, nums: List[int]) -> int:
    def maxProduct(self, nums):
        MinTemp = nums[0]
        MaxTemp = nums[0]
        Max = nums[0]
        for i in range(1, len(nums)):
            MinTemp, MaxTemp = min(nums[i], nums[i] * MaxTemp, nums[i] * MinTemp), max(nums[i], nums[i] * MaxTemp, nums[i] * MinTemp)
            Max = max(Max, MaxTemp)
        return Max

def main():
    nums = [2,3,-2,4]        #expect is 6
    obj = Solution()
    result = obj.maxProduct(nums)
    print("return result is :",result)
    
if __name__ =='__main__':
    main()   