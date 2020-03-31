# leetcode time     cost : 1254 ms
# leetcode memory   cost : 26.4 MB 
# Time  Complexity: O(steps*maxMovingLength)
# Space Complexity: O(steps*maxMovingLength)
# solution 1.DP. f[i][j] 表示在进行了 i 次操作后，指针位置为 j 的方案数.
# f[i][j] = f[i - 1][j - 1] + f[i - 1][j] + f[i - 1][j + 1]
# 需要注意j在2头端点的情况
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        arrLen = min(arrLen, steps + 1)
        f = [[0] * arrLen for _ in range(steps + 1)]
        f[0][0] = 1
        for i in range(1, steps + 1):
            for j in range(arrLen):
                for k in [-1, 0, 1]:
                    if 0 <= j - k < arrLen:
                        f[i][j] += f[i - 1][j - k]
        return f[steps][0] % (10**9 + 7)