# leetcode time     cost : 192 ms
# leetcode memory   cost : 15.7 MB 
# Time  Complexity: O(logN)
# Space Complexity: O(logN)
# solution 2,Trie
class Trie:
    def __init__(self):
        self.Trie = {}

    def insert(self, word):
        curr = self.Trie
        for w in word:
            if w not in curr:
                curr[w] = {}
            curr = curr[w]
        curr['#'] = 1
        
    def isTail(self, word):
        curr = self.Trie
        for w in word:
            curr = curr[w]
        return len(curr) == 1

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = Trie()
        cnt = 0
        words = set(words)
        for word in words:
            trie.insert(word[::-1])
        for word in words:
            if trie.isTail(word[::-1]):
                cnt += len(word) + 1
        return cnt

def main():
    words = ["time", "me", "bell"]      #expect is 10
    obj = Solution()
    res = obj.minimumLengthEncoding(words)
    assert res == 10
    
    
if __name__ =='__main__':
    main() 