# solution 1, 
# 26 binary system into decimal
class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        bit = 1
        for a in s[::-1]:
            res += (ord(a) - 64) * bit
            bit *= 26
        return res