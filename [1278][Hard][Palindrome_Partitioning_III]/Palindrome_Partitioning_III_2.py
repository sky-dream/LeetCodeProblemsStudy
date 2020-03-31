# leetcode time     cost : 232 ms
# leetcode memory   cost : 13.9 MB 
# Time  Complexity: O(N**3 *K)
# Space Complexity: O(N**2 + NK)
# solution 1, DP, with pre data process
# 我们用 f[i][j] 表示对于字符串 S 的前 i 个字符，将它分割成 j 个非空且不相交的回文串，最少需要修改的字符数
# 预处理出所有的 cost(S, l, r)，在后续调用 cost() 函数时，我们只需要 O(1) 的时间便可以返回结果
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        cost = [[0] * n for _ in range(n)]
        for span in range(2, n + 1):
            for i in range(n - span + 1):
                j = i + span - 1
                cost[i][j] = cost[i + 1][j - 1] + (0 if s[i] == s[j] else 1)

        f = [[10**9] * (k + 1) for _ in range(n + 1)]
        f[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, min(k, i) + 1):
                if j == 1:
                    f[i][j] = cost[0][i - 1]
                else:
                    for i0 in range(j - 1, i):
                        f[i][j] = min(f[i][j], f[i0][j - 1] + cost[i0][i - 1])
        
        return f[n][k]