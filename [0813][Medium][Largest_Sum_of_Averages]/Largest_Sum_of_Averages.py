# leetcode time     cost : 592 ms
# leetcode memory   cost : 13.6 MB 
# Time  Complexity: O(N*N*K)
# Space Complexity: O(N*K)
# solution 1.DP. 
# 设 dp(i, k) 表示数组 A 中从第 i 个元素到结尾 A[i:] 分成 k 个相邻的非空子数组，可以得到的最大分数
from typing import List
class Solution(object):
    def largestSumOfAverages(self, A, K):
        P = [0]
        for x in A: P.append(P[-1] + x)
        def average(i, j):
            return (P[j] - P[i]) / float(j - i)

        N = len(A)
        dp = [average(i, N) for i in range(N)]
        for k in range(K-1):
            for i in range(N):
                for j in range(i+1, N):
                    dp[i] = max(dp[i], average(i, j) + dp[j])

        return dp[0]

def main():
    A, K = [9,1,2,3,9],3      #expect is 20
    obj = Solution()
    res = obj.largestSumOfAverages(A, K)
    print("return value is ",res);
    
if __name__ =='__main__':
    main()   