# -*- coding: utf-8 -*-  
# leetcode time     cost : 32 ms
# leetcode memory   cost : 13.6 MB
# Time  Complexity: O(N*N)
# Space Complexity: O(N)
#solution 3, BFS
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        visited = [0]*(len(s)+1)
        wordSet = set(wordDict)
        queue = []
        queue.append(0)
        while (queue):
            start = queue.pop(0)
            if (visited[start] == 0):
                for j in range(start+1,len(s)+1):
                    if (s[start:j] in wordSet):
                        queue.append(j)
                        if (j == len(s)):
                            return True
                visited[start] = 1
        return False