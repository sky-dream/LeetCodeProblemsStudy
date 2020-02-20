#-*- coding: utf-8 -*-  
# leetcode time     cost : 184 ms
# leetcode memory   cost : 35.5 MB 
import time
class Solution:
    def findMaximumXOR(self, nums):
            ans = 0
            for i in reversed(range(32)):
                prefixes = set([x >> i for x in nums])
                ans <<=1
                candidate = ans + 1
                for p in prefixes:
                    if candidate ^ p in prefixes:
                # or use if any(candidate^p in prefixes for p in prefixes):
                        ans = candidate
                        break      
            return ans   

def main():
    obj = Solution()
    nums = [3,10,5,25,2,8]      # expect is 28
    result = obj.findMaximumXOR(nums)
    print(result)
    
if __name__ =='__main__':
    main()  