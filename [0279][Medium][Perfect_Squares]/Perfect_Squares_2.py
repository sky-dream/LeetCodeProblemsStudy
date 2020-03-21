#-*- coding: utf-8 -*-  
# leetcode time     cost : 7156 ms
# leetcode memory   cost : 13.6 MB
# Time  Complexity: O(N)
# Space Complexity: O(N)
# solution 2, DP
import math
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')]*(n + 1) # 默认初始化值都为0
        for i in range(n+1):
            dp[i] = i # 最坏的情况就是每次+1
            for j in range(i+1):  # i可能是平方数，eg,16,9,    
            # eg,19 = 9+9+1 = 16+1+1+1，
                if i - j*j >= 0:
                    dp[i] = min(dp[i], dp[i - j*j] + 1) # 动态转移方程
                else: break
        return dp[n]

def main():
    n = 16      #expect is 2 
    obj = Solution()
    res = obj.numSquares(n)
    print("return value is ",res);
    
if __name__ =='__main__':
    main() 