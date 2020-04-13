# -*- coding: utf-8 -*-
# leetcode time     cost : 1864 ms
# leetcode memory   cost : 13.8 MB
# Time  Complexity: O(N*N)
# Space Complexity: O(N)
# The knows API is already defined for you.
# return a bool, whether a knows b


def knows(a: int, b: int):
    pass
# solution 1 optimized


class Solution:
    def findCelebrity(self, n: int):
        if not n or n < 0:
            return -1
        for i in range(n):
            if self.is_celeb(i, n):
                return i
        return -1

    def is_celeb(self, i, n):
        for j in range(n):
            if i == j:
                continue
            if knows(i, j) or not knows(j, i):
                return False
        return True
