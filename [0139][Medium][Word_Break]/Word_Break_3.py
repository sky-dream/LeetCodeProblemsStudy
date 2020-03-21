# -*- coding: utf-8 -*-  
# leetcode time     cost : 48 ms
# leetcode memory   cost : 13.7 MB
# Time  Complexity: O(N*N)
# Space Complexity: O(N)
#solution 4, DP
class Solution:
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        dp = [False]*(len(s)+1)
        wordSet = set(wordDict)
        dp[0] = True
        for i in range(1,len(s)+1):
            for j in range(i,-1,-1):
                if (dp[j] and s[j:i] in wordSet):
                    dp[i] = True;
                    break;
        return dp[-1]

def main():
    s, wordDict = "catsanddog",["cat","cats","and","sand","dog"]            #expect is True
    obj = Solution()
    result = obj.wordBreak(s, wordDict)
    print("return result is :",result)
    
if __name__ =='__main__':
    main() 