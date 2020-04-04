from typing import List
# leetcode time     cost : 160 ms
# leetcode memory   cost : 13.6 MB 
# solution 1. dp
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        # 初始值设为最大
        dp = [[float('inf') for _ in range(n)] for _ in range(n)]
        # 初始区间查询最大值设为0
        maxval = [[0 for _ in range(n)] for _ in range(n)]
        # 求区间[i, j]中最大元素
        for i in range(n):
            for j in range(i, n):
                maxval[i][j] = max(arr[i:j + 1])
        # 叶子结点不参与计算
        for i in range(n):
            dp[i][i] = 0
        # 枚举区间长度length
        for l in range(1, n):
            # 枚举区间起始点start
            for s in range(n - l):
                # 枚举划分两棵子树
                for k in range(s, s + l):
                    dp[s][s + l] = min(dp[s][s + l], dp[s][k] + dp[k + 1][s + l] + maxval[s][k] * maxval[k + 1][s + l])
        return dp[0][n - 1]
    
def main():
    arr = [6,2,4]        # expect is 32
    obj = Solution()
    result = obj.mctFromLeafValues(arr)
    print("return result is :",result)
    
if __name__ =='__main__':
    main() 