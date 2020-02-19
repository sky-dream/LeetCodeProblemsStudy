# https://leetcode.com/problems/word-search-ii/discuss/59790/Python-dfs-solution-(directly-use-Trie-implemented).
# leetcode time     cost : 484 ms
# leetcode memory   cost : 52.2 MB 
import collections
class Node:
    def __init__(self):
        self.chars = {}
        self.word = False

class Trie:
    def __init__(self):
        self.node = Node()

    def add_word(self, word):
        node = self.node
        for c in word:
            if c not in node.chars:
                node.chars[c] = Node()
            node = node.chars[c]
        node.word = True

class Solution:
    def findWords(self, board, words):
        res = []
        trie = Trie()
        for word in words:
            trie.add_word(word)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, trie.node, res, "", i, j)
        return res

    def dfs(self, board, trie, res, word, i, j):
        if trie.word:
            res.append(word)
            trie.word = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        if not trie:
            return 
        char = board[i][j]
        if char in trie.chars:
            board[i][j] = '#'
            trie = trie.chars[char]
            for x, y in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
                self.dfs(board, trie, res, word + char, i + x, y + j)
            board[i][j] = char

def main():
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]] 
    words = ["oath","pea","eat","rain"]             #expect is ["oath","eat"]
    obj = Solution()
    result = obj.findWords(board, words)
    assert result == ["oath","eat"], ["hint: result is wrong"]
    print("return result is :",result)
    
if __name__ =='__main__':
    main() 