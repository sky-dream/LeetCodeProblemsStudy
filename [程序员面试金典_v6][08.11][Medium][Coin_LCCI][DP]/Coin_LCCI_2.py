# leetcode time     cost : 56 ms
# leetcode memory   cost : 13.6 MB
# solution 2, math
class Solution:
    def waysToChange(self, n: int) -> int:
        mod = 10**9 + 7

        ans = 0
        for i in range(n // 25 + 1):
            rest = n - i * 25
            a, b = rest // 10, rest % 10 // 5
            ans += (a + 1) * (a + b + 1)
        return ans % mod
