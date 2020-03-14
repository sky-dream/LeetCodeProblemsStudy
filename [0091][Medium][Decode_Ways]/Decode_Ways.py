# -*- coding: utf-8 -*-  
# leetcode time     cost : 36 ms
# leetcode memory   cost : 13.7 MB
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # dp[i] is when come to i element s[i-1], the possible decode kinds
        dp = [0]*(n+1)

        # no need check none since s is a non-empty string
        if n>=1: 
            dp[0] = 1 

        # start with more than 3 bit, loop i from 2 to (n)
        for i in range(1,n+1):

            # important,check whether s[i] can be a individual char, if yes, need add possible of dp[i-1]
            # if xx0xx, the 0 must be combined with before , should not add dp[i-1]       
            if 1<= int(s[i-1]) <= 9:
                dp[i] += dp[i-1] 

            # check whether s[i] can be a combined char, if yes, need add possible of  dp[i-2]       
            # wrong example: if  i>1 and 1<= int(s[i-2]) <= 2 and 0<= int(s[i-1]) <= 6:
            if  i>=2 and 10 <= int(s[i-2])*10 + int(s[i-1]) <= 26:
                dp[i] +=  dp[i-2]

        print(dp)                
        return dp[n]

def main():
    code = "226"             #expect is 3
    obj = Solution()
    result = obj.numDecodings(code)
    print("return result is :",result)
    
if __name__ =='__main__':
    main()   