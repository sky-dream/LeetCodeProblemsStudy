# -*- coding: utf-8 -*-  
# leetcode time     cost : max time exceeded.
# leetcode memory   cost : -- MB
# Time  Complexity: O(T∗logT)
# Space Complexity: O(T)
# solution 5, normal dp
# https://www.bilibili.com/video/av31335074?from=search&seid=10692494204428529428
class Solution(object):
    def racecar(self, target):
        # try all possible positions to 'restart' with speed 1 or -1.
        # dp[i][d] is the min step come to position i with direction d, d=0 is forward, d=1 is backward
        dp = [[0]*2 for i in range(2*target+1)]
        for t in range(1, target + 1):
            k = t.bit_length()
            if t == 2**k - 1:
                dp[t][0] = k
                dp[t][1] = k+1 # turn back
                continue
            left = 2**k - 1 - t
            dp[t][0] = k+1+min(dp[left][1], dp[left][0]+1)
            dp[t][1] = k+1+min(dp[left][0], dp[left][1]+1)
            # loop all dp status from 1 to position t.
            for i in range(1,t):
                for d in range(2):
                    dp[t][d] = min(dp[t][d], min( \
                                dp[i][0] +2 +dp[t-i][d], \
                                dp[i][1] +1 +dp[t-i][d] ))   
        return min(dp[target][0],dp[target][1])


def main():
    target = 16      #expect is 7  
    obj = Solution()
    res = obj.racecar(target)
    print("return value is ",res);
    
if __name__ =='__main__':
    main() 