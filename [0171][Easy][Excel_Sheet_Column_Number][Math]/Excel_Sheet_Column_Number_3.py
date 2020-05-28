#solution 3, 
# 26 binary system into decimal,use sum
class Solution:
    def titleToNumber(self, s: str) -> int:
        return sum( (ord(a) - 64) * (26 ** i)  for i, a in enumerate(s[::-1]))