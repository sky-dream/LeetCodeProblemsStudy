# leetcode time     cost : 40 ms
# leetcode memory   cost : 13.9 MB 
# Time  Complexity: O(n)
# Space Complexity: O(1)
# solution 2, 数学分析，所有counter的最大公约数x > 2时， 有解， 否则为 False
import collections
from functools import reduce
# reduce(function, iterable[, initializer])
class Solution(object):
    def hasGroupsSizeX(self, deck):
        from fractions import gcd
        vals = collections.Counter(deck).values()
        return reduce(gcd, vals) >= 2