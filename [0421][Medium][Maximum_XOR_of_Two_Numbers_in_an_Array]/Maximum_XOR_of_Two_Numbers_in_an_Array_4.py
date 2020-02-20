#-*- coding: utf-8 -*-  
# leetcode time     cost : 120 ms
# leetcode memory   cost : 13.7 MB 
'''
General form of solution is to find two numbers which have the highest bits complementing each other (0 and 1). 
Then store that max, look at the next less significant bit and see if another two numbers complement each other 
(which includes the bits sets from the previous max). If so, this number will
be greater than the previous maximum. Steps:

Find the new possible maximum by setting the next bit to 1 on the current maximum
use a mask with all 1s up to the current bit i and & all numbers with this mask to see which bit in that number up to bit i are set as 1.
Critical part: to solve this in O(n) it's important to know that If a ^ b = c, 
then a ^ c = b and c ^ b = a. So, if we are looking for a particular number (in our case a possible maximum) we can do the following search: 
iterate in the numbers that we &'d with the mask. If our potental maximum is c, and our current number is a, 
we're looking for another number b that XOR'd with a gives c. Since we also know from above that a ^ c = b, 
we can just look for b it directly in our numbers (i.e. b = a ^ c, or in my code, bit ^ possible_mx).
'''
class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx,mask=0,0
        for i in range(31,-1,-1):
            possible_mx = mx | 1 << i
            mask = mask | 1 << i
            bits=set()
            for num in nums:
                bits.add(num & mask)
            for bit in bits:
                if bit ^ possible_mx in bits:
                    mx = possible_mx
                    break
        return mx 

def main():
    obj = Solution()
    nums = [3,10,5,25,2,8]      # expect is 28
    result = obj.findMaximumXOR(nums)
    print(result)
    
if __name__ =='__main__':
    main()  