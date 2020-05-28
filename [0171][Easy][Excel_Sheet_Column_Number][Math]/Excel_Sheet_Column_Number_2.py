# solution 2,
# 26 binary system into decimal,use func tool
import functools
class Solution:
    def titleToNumber(self, s: str) -> int:
        return functools.reduce(lambda x, y: x * 26 + y, [ord(a) - 64 for a in s ])