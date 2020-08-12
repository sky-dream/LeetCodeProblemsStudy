# leetcode time     cost : 60 ms
# leetcode memory   cost : 13.6 MB 
# solution 2, DP from right to left for the text
class Solution(object):
    def isMatch(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or (first_match and dp[i+1][j]) # priority: not > and > or
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]

        return dp[0][0]