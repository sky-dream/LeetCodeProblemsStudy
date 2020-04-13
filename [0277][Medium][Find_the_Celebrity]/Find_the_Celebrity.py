# -*- coding: utf-8 -*-
# leetcode time     cost : maximum time exceeded
# leetcode memory   cost : --- MB
# Time  Complexity: O(N*N)
# Space Complexity: O(N)

# The knows API is already defined for you.
# return a bool, whether a knows b


def knows(a: int, b: int):
    pass
# solution 1


class Solution:
    def findCelebrity(self, n: int) -> int:
        if not n:
            return -1
        celeb_map = {}
        ans = -1
        for i in range(n):
            celeb_map[i] = True
        for i in range(n - 1):
            for j in range(i + 1, n):
                if knows(i, j):
                    celeb_map[i] = False
                else:
                    celeb_map[j] = False
                if knows(j, i):
                    celeb_map[j] = False
                else:
                    celeb_map[i] = False
        for key, val in celeb_map.items():
            if val == True:
                if ans != -1:
                    return -1
                ans = key
        return ans
