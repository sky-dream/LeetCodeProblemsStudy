# leetcode time     cost : 52 ms
# leetcode memory   cost : 13.9 MB 
# Time  Complexity: O(N*logN)
# Space Complexity: O(N)
# slolution 4, DP and binarySearch with bisect lib,
import bisect
class Solution:
    #def lengthOfLIS(self, nums: List[int]) -> int:
    def lengthOfLIS(self, nums):
        # minend[i] is the minimum ending of an increasing subsequence of length i+1.
        minend = [float('inf')] * (len(nums) + 1)
        for num in nums:
            minend[bisect.bisect_left(minend, num)] = num
            # at last, minend is [1, 3, 4, 5, 6, 10, inf, inf, inf, inf]
        # to find the first elment of float('inf') in the minend[], just the max length index     
        return minend.index(float('inf'))
    
    def lengthOfLIS_2(self, nums):
        minend = [float('inf')] * len(nums)
        for num in nums:
            minend[bisect.bisect_left(minend, num)] = num
        return bisect.bisect_left(minend, float('inf'))

def main():
    nums = [1,3,6,7,9,4,10,5,6] #expect is 6
    obj = Solution()
    result = obj.lengthOfLIS(nums)
    print("return result is "+str(result));

if __name__ =='__main__':
    main() 