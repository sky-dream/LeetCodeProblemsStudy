#-*- coding: utf-8 -*-  
# leetcode time     cost : 200 ms
# leetcode memory   cost : 35.7 MB 
class Solution:
    def findMaximumXOR(self, nums):
        answer = 0
        for i in range(32)[::-1]:
            answer <<= 1
            prefixes = {num >> i for num in nums}   # prefixes is a set of list element diveded by 2^i,
            # a xor b xor a = b, a xor a = 0
            answer += any(answer^1 ^ p in prefixes for p in prefixes)
        return answer

def main():
    obj = Solution()
    nums = [3,10,5,25,2,8]      # expect is 28
    result = obj.findMaximumXOR(nums)
    print(result)
    
if __name__ =='__main__':
    main()  