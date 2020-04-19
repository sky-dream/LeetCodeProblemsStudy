# -*- coding: utf-8 -*-  
# leetcode time     cost : 36 ms
# leetcode memory   cost : 13.7 MB
# Time  Complexity: O(len(s1)*len(s2))
# Space Complexity: O(len(s2))
# The main idea is to find a circle. A circle means m rounds of s1 has a subarray of n rounds of s2, 
# and at the meantime starting from the same point of s1.
class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        start = {} # s2_idx : s1_round, s2_round
        s1_round, s2_round, s2_idx = 0, 0, 0
        while s1_round < n1:
            s1_round += 1
            for ch in s1:
                if ch == s2[s2_idx]:
                    s2_idx += 1
                    if s2_idx == len(s2):
                        s2_round += 1
                        s2_idx = 0
            if s2_idx in start:
                prev_s1_round, prev_s2_round = start[s2_idx]
                circle_s1_round, circle_s2_round = s1_round - prev_s1_round, s2_round - prev_s2_round
                res = (n1 - prev_s1_round) // circle_s1_round * circle_s2_round
                left_s1_round = (n1 - prev_s1_round) % circle_s1_round + prev_s1_round
                for key, val in start.items():
                    if val[0] == left_s1_round:
                        res += val[1]
                        break
                return res // n2
            else:
                start[s2_idx] = (s1_round, s2_round)
        return s2_round // n2