# -*- coding: utf-8 -*-  
# solution 1, brute force calculation.
# leetcode time     cost : 116 ms
# leetcode memory   cost : 12 MB 
# Time  Complexity: O(2^{2n})
# Space Complexity: O(2^{2n})
'''
We can generate all 2^{2n} sequences of '(' and ')' characters. 
Then, we will check if each one is valid.

To generate all sequences, we use a recursion. 
All sequences of length n is just '(' plus all sequences of length n-1, 
and then ')' plus all sequences of length n-1.

To check whether a sequence is valid, we keep track of balance, 
the net number of opening brackets minus closing brackets. 
If it falls below zero at any time, or doesn't end in zero, 
the sequence is invalid - otherwise it is valid.
'''
class Solution(object):
    def generateParenthesis(self, n):
        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate()
        return ans