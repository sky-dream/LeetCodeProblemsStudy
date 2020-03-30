# leetcode time     cost : 320 ms
# leetcode memory   cost : 13.5 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
# solution 1 DP,
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        f,g = {},{}
        max_mod= 10**9+7
        dlist = ['a', 'e', 'i', 'o', 'u']
        # 初始各个元音方案数置1
        for i in dlist:
            f[i] = 1
        # 按照描述模拟 (n-1) 次
        for i in range(0,n-1):
            g = {}
            for i in dlist:
                g[i] = 0
            g['e'] += f['a'] + f['i']
            g['a'] += f['e'] + f['i'] + f['u']
            g['i'] += f['e'] + f['o']
            g['o'] += f['i']
            g['u'] += f['i'] + f['o']
            for i in dlist:
                f[i] = g[i] % max_mod
        return sum(f.values()) % max_mod