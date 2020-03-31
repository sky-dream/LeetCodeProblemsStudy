# leetcode time     cost : 1756 ms
# leetcode memory   cost : 13.8 MB 
# Time  Complexity: O(N**3 *K)
# Space Complexity: O(NK)
# solution 1, DP,
# 我们用 f[i][j] 表示对于字符串 S 的前 i 个字符，将它分割成 j 个非空且不相交的回文串，最少需要修改的字符数
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        def cost(l, r):
            ret, i, j = 0, l, r
            while i < j:
                ret += (0 if s[i] == s[j] else 1)
                i += 1
                j -= 1
            return ret
        
        n = len(s)
        f = [[10**9] * (k + 1) for _ in range(n + 1)]
        f[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, min(k, i) + 1):
                if j == 1:
                    f[i][j] = cost(0, i - 1)
                else:
                    for i0 in range(j - 1, i):
                        f[i][j] = min(f[i][j], f[i0][j - 1] + cost(i0, i - 1))
        
        return f[n][k]