#-*- coding: utf-8 -*-  
# leetcode time     cost : 200 ms
# leetcode memory   cost : 35.7 MB 
class Solution:
    def findMaximumXOR(self, nums):
        answer = 0
        for i in range(32)[::-1]:
            tmp = set()
            answer <<= 1
            prefixes = {num >> i for num in nums}   # prefixes is a set of list element divided by 2^i,
            # concentrated version: 
            answer += any(answer^1 ^ p in prefixes for p in prefixes)
        return answer
    
    def findMaximumXOR_1(self, nums):
        answer = 0
        for i in range(32)[::-1]:
            tmp = set()
            answer <<= 1
            prefixes = {num >> i for num in nums}   # prefixes is a set of list element divided by 2^i,
            # divide it to sub problems, get answer from all nums bit 31, from all nums bit 31-30, bit 31-29....
            # detailed version
            for p in prefixes:
                # answer^1 is used to pre set current bit 0 to 1 to find the matched(bit0=0,higher bits is opposite) in the prefixes 
                # if p and answer^1^p both in the prefixes,then the 2 value can be add to tmp set, sum them is the max bit=1 num.
                if (answer^1^p in prefixes):    # the same as (answer + 1)^p
                    # eg, (answer,(answer<<1)^1) is (0,1),(1,3),(3,7),(7,15),(14,29)...
                    tmp.add(answer^1 ^ p)
            # then sum all answers from all nums bit 31, bit 31-30, bit 31-29.....
            answer += any(tmp)
            if answer: print("when iterate to bit:",i,",prefixes set is:",prefixes,",tmp is:",tmp,",answer is:",answer) 
        return answer    

def main():
    obj = Solution()
    nums = [3,10,5,25,2,8]      # expect is 28
    result = obj.findMaximumXOR(nums)
    print(result)
    
if __name__ =='__main__':
    main()