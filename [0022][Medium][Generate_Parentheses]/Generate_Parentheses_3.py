# -*- coding: utf-8 -*-  
# solution 3, Closure Number.
# leetcode time     cost : 28 ms
# leetcode memory   cost : 12 MB 
# Time  Complexity: O(2^{2n}/srt(n))
# Space Complexity: O(2^{2n}/srt(n))
'''
To enumerate something, generally we would like to express it as a sum of disjoint subsets that are easier to count.

Consider the closure number of a valid parentheses sequence S: 
the least index >= 0 so that S[0], S[1], ..., S[2*index+1] is valid. 
Clearly, every parentheses sequence has a unique closure number. 
We can try to enumerate them individually.

For each closure number c, we know the starting and ending brackets must be at index 0 and 2*c + 1. 
Then, the 2*c elements between must be a valid sequence, plus the rest of the elements must be a valid sequence.
'''
class Solution(object):
    def generateParenthesis(self, N):
        if N == 0: return ['']
        ans = []
        for c in xrange(N):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(N-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans