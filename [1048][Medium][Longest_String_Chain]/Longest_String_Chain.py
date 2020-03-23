# leetcode time     cost : 152 ms
# leetcode memory   cost : 13.5 MB 
# Time  Complexity: O(MN)
# Space Complexity: O(MN)
# solution 1 DP.
class Solution:
    def longestStrChain(self, words):
        words.sort(key=len)
        note={}
        maxChain=1
        for word in words:
            if word not in note:
                note[word]=1
            for i in range(0,len(word)):
                newWord=word[:i]+word[i+1:]
                if (newWord) in note:
                    note[word]=max(note[word],note[newWord]+1)
            maxChain=max(maxChain,note[word])
        return maxChain