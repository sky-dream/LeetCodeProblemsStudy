# -*- coding: utf-8 -*-  
# leetcode time     cost : 936 ms
# leetcode memory   cost : 16.8 MB
# solution 1, recursion with memo, DP
class Solution:
    def strangePrinter(self, S):
        memo = {}
        def dp(i, j):
            if i > j: return 0
            if (i, j) not in memo:
                memo[i, j] = dp(i+1, j) + 1
                for k in range(i+1, j+1):
                    if S[k] == S[i]:
                        memo[i, j] = min(memo[i, j], dp(i, k-1) + dp(k+1, j))
            return memo[i, j]

        return dp(0, len(S) - 1)


def main():
    word1 = "aaabbb"  # ans 2
    obj = Solution()
    res = obj.strangePrinter(word1)
    print("return value is ",res)
    
if __name__ =='__main__':
    main() 