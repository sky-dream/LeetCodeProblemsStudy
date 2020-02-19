# https://leetcode.com/problems/word-search-ii/discuss/59852/Clean-python-code-with-Trie
# leetcode time     cost : 424 ms
# leetcode memory   cost : 47.6 MB 
from collections import defaultdict
class TrieNode(object):
    def __init__(self):
        self.word = None
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        for char in word:
            root = root.children.setdefault(char, TrieNode())
        root.word = word


class Solution(object):
    def search(self, i, j, root, board, m, n, r):
        char = board[i][j]
        if not (char and char in root.children):
            return

        board[i][j], root = None, root.children[char]

        if root.word:
            r.append(root.word)
            root.word = None

        for x, y in ((0, -1), (-1, 0), (0, 1), (1, 0)):
            ii, jj = i + x, j + y
            if 0 <= ii < m and 0 <= jj < n:
                self.search(ii, jj, root, board, m, n, r)

        board[i][j] = char

    def findWords(self, board, words):
        if not board:
            return []

        tree = Trie()
        [tree.insert(word) for word in words]

        m, n, r = len(board), len(board[0]), []

        for i, row in enumerate(board):
            for j, char in enumerate(row):
                self.search(i, j, tree.root, board, m, n, r)
        return r

def main():
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]] 
    words = ["oath","pea","eat","rain"]             #expect is ["oath","eat"]
    obj = Solution()
    result = obj.findWords(board, words)
    assert result == ["oath","eat"], ["hint: result is wrong"]
    print("return result is :",result)
    
if __name__ =='__main__':
    main() 