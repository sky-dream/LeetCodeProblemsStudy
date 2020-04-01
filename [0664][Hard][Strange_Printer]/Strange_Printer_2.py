# -*- coding: utf-8 -*-  
# leetcode time     cost : 664 ms
# leetcode memory   cost : 13.9 MB
# solution 2, interval problem DP
class Solution:
    def strangePrinter(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        dp = [[0]*(n+1) for i in range(n+1)]
        # dp[l][r], the min print turn for s[l:r+1]
        for i in range(1, n+1):
            for l in range(n):
                # 计算的时候保证小的已经算出来了
                if i + l - 1 < n:
                    r = l + i -1
                    dp[l][r] = dp[l+1][r] + 1
                    for k in range(l+1, r+1):
                        if s[k] == s[l]:
                            dp[l][r] = min(dp[l][r], dp[l][k-1]+dp[k+1][r])
        return dp[0][n-1]


def main():
    word1 = "aaabbb"  # ans 2
    obj = Solution()
    res = obj.strangePrinter(word1)
    print("return value is ",res)
    
if __name__ =='__main__':
    main() 