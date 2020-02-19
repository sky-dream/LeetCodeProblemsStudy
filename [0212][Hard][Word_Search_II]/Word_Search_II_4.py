# https://leetcode.com/problems/word-search-ii/discuss/59852/Clean-python-code-with-Trie
# leetcode time     cost : 492 ms
# leetcode memory   cost : 52.1 MB 
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.nodes = defaultdict(TrieNode)
        self.word = None
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        tn = self.root   # tn = TrieNode
        for c in word:
            tn = tn.nodes[c]
        tn.word = word
        
class Solution(object):
    def findWords(self, board, words):
        trie = Trie()
        for w in words:
            trie.insert(w)
        
        tn = trie.root
        res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(i, j, board, tn, res)
        return res
    
    def dfs(self, i, j, board, tn, res):
        if tn.word:
            res.append(tn.word)
            tn.word = None # rain and rainy in words

        if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] in tn.nodes:
            c = board[i][j]
            board[i][j] = '#'
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                self.dfs(i+x, j+y, board, tn.nodes[c], res)
            board[i][j] = c

def main():
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]] 
    words = ["oath","pea","eat","rain"]             #expect is ["oath","eat"]
    obj = Solution()
    result = obj.findWords(board, words)
    assert result == ["oath","eat"], ["hint: result is wrong"]
    print("return result is :",result)
    
if __name__ =='__main__':
    main() 