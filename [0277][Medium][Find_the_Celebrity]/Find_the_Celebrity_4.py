# -*- coding: utf-8 -*-
# leetcode time     cost : 1612 ms
# leetcode memory   cost : 14 MB
# Time  Complexity: O(N)
# Space Complexity: O(N)
# The knows API is already defined for you.
# return a bool, whether a knows b


def knows(a: int, b: int):
    pass
# solution 4


class Solution:
    def findCelebrity(self, n):
        if not n or n < 0:
            return -1
        celeb = 0
        memo = {}
        for i in range(1, n):
            if knows(celeb, i):
                memo[(celeb, i)] = True
                celeb = i
            else:
                memo[(celeb, i)] = False
        return self.is_celeb(celeb, n, memo)

    def is_celeb(self, celeb, n, memo):
        for i in range(n):
            if celeb == i:
                continue
            if (celeb, i) in memo and memo[(celeb, i)]:
                return -1
            if (i, celeb) in memo and not memo[(i, celeb)]:
                return -1
            if knows(celeb, i) or not knows(i, celeb):
                return -1
        return celeb
