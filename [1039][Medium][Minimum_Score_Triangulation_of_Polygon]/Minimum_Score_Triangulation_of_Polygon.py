# leetcode time     cost : 140 ms
# leetcode memory   cost : 13.7 MB
# Time  Complexity: O(N**3)
# Space Complexity: O(N**2)
# solution 1,DP
class Solution(object):
    def minScoreTriangulation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        len_a = len(A)
        min_score = float('inf')
        dp = [[float('inf')]*len_a for _ in range(len_a)]

        for i in range(0, len_a-1):
            dp[i][i+1] = 0   # 相邻2点的边无法构成三角形
        # 遍历所有可能与某一条边构成三角形的 第3个顶点 与起始点 间隔
        for d in range(2, len_a): 
        # 将边界带入 然后看是否符合含义  比如此时边界值是len_a - 1 然后带入发现 i只有一个选项是0  j的选项是len_a - 1
            # 遍历所有可能的三角形起始点
            for i in range(0, len_a-d):
                # 计算三角形终结点
                j = d + i 
                # 遍历所有可能的小区间拆分方式
                for k in range(i+1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + A[i]*A[k]*A[j])
        return dp[0][len_a-1]