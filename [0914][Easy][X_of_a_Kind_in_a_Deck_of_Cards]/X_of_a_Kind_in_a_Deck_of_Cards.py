# leetcode time     cost : 52 ms
# leetcode memory   cost : 13.8 MB 
# Time  Complexity: O(n)
# Space Complexity: O(1)
# solution 1， brute force
import collections
class Solution(object):
    def hasGroupsSizeX(self, deck):
        count = collections.Counter(deck)
        N = len(deck)
        for X in range(2, N+1):
            if N % X == 0:
                if all(v % X == 0 for v in count.values()):
                    return True
        return False