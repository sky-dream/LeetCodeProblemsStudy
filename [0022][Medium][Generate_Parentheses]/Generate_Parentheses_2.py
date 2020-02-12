# -*- coding: utf-8 -*-  
# solution 2, Backtracking.
# leetcode time     cost : 24 ms
# leetcode memory   cost : 12 MB 
# Time  Complexity: O(2^{2n}/srt(n))
# Space Complexity: O(2^{2n}/srt(n))
'''
Instead of adding '(' or ')' every time as in Approach 1, 
let's only add them when we know it will remain a valid sequence. 
We can do this by keeping track of the number of opening and closing brackets we have placed so far.
We can start an opening bracket if we still have one (of n) left to place. 
And we can start a closing bracket if it would not exceed the number of opening brackets.
'''
class Solution(object):
    def generateParenthesis(self, N):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans