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
    def titleToNumber_2(self, s: str) -> int:
        res = 0
        # ord("A") is 65,
        for char in s:
            res = (ord(char) - 64) + res*26
        return res    