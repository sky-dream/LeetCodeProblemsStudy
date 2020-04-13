# -*- coding: utf-8 -*-
# leetcode time     cost : 1384 ms
# leetcode memory   cost : 13.6 MB
# Time  Complexity: O(N)
# Space Complexity: O(N)
# The knows API is already defined for you.
# return a bool, whether a knows b


def knows(a: int, b: int):
    pass

# solution 3


class Solution:
    def findCelebrity(self, n: int):
        celebrity = 0
        for i in range(1, n):
            if knows(celebrity, i):
                                # 说明当前的这个celebrity肯定不是名人，因为他认识别的人
                celebrity = i
                # 到这里的 celebrity，必定不认识 [celebrity + 1, n - 1]的所有人
        for i in range(celebrity):
            if knows(celebrity, i):  # 为了确保celebrity 不认识 [0, celebrity - 1]
                return -1

        for i in range(n):
            if not knows(i, celebrity):  # 为了确保 每个人都认识 celebrity
                return -1
        return celebrity
