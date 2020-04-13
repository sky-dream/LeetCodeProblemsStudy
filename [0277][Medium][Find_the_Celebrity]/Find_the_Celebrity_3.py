# -*- coding: utf-8 -*-
# leetcode time     cost : 1600 ms
# leetcode memory   cost : 13.7 MB
# Time  Complexity: O(N)
# Space Complexity: O(N)
# The knows API is already defined for you.
# return a bool, whether a knows b


def knows(a: int, b: int):
    pass


class Solution:
    def findCelebrity(self, n):
        if not n:
            return -1
        celeb = 0
        for i in range(1, n):
            if knows(celeb, i):
                celeb = i
        for i in range(n):
            if i == celeb:
                continue
            if not knows(i, celeb) or knows(celeb, i):
                return -1
        return celeb
