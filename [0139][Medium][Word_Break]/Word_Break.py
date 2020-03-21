# -*- coding: utf-8 -*-  
# leetcode time     cost : 50 ms
# leetcode memory   cost : 15 MB
# Time  Complexity: O(N*N)
# Space Complexity: O(N)
#solution 2, recursion and memorize
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [False]*(len(s)+1)
        wordSet = set(wordDict)
        return self.word_BreakHelper(s, wordSet, 0, memo)

    def word_BreakHelper(self,s, wordSet, start, memo):
        if (start == len(s)):
            return True
        
        if (memo[start] != False):
            return memo[start]
        
        for j in range(start+1,len(s)+1):
            if (s[start:j] in wordSet and self.word_BreakHelper(s, wordSet, j, memo)):
                # s[0:4] only include s[0-3],
                # print(s[start:j],memo,start,j)
                memo[start] = True
                return memo[start]
        memo[start] = False
        return memo[start]