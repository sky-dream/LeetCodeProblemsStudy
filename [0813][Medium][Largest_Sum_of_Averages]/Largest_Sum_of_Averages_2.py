# leetcode time     cost : 388 ms
# leetcode memory   cost : 13.8 MB 
# Time  Complexity: O(N*N*K)
# Space Complexity: O(N*K)
# solution 1.DP. 
# 设 dp(i, k) 表示将数组 A 中的前 i 个元素 A[:i] 分成 k 个相邻的非空子数组，可以得到的最大分数
from typing import List
class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        N = len(A)
        p = [0]
        for i in A: p.append(p[-1] + i)
        def avg(i, j):
            return (p[j] - p[i]) / float(j - i)
        dp = [[0.0 for _ in range(N+1)] for _ in range(K+1)]
        for i in range(1, N+1):
            dp[1][i] = avg(0, i)
        for k in range(2, K+1):
            for i in range(k, N+1):
                for j in range(k-1, i):
                    dp[k][i] = max(dp[k][i], dp[k-1][j] + avg(j, i))
        return dp[-1][-1]

def main():
    A, K = [9,1,2,3,9],3      #expect is 20
    obj = Solution()
    res = obj.largestSumOfAverages(A, K)
    print("return value is ",res);
    
if __name__ =='__main__':
    main()   