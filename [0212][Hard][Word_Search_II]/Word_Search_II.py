# https://leetcode.com/problems/word-search-ii/discuss/59804/27-lines-uses-complex-numbers
# leetcode time     cost : 444 ms
# leetcode memory   cost : 43.4 MB 
class Solution:
    #  def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    def findWords(self, board, words):

        root = {}
        for word in words:
            node = root
            for c in word:
                node = node.setdefault(c, {})
            node[None] = True
        board = {i + 1j*j: c
                 for i, row in enumerate(board)
                 for j, c in enumerate(row)}

        found = []
        def search(node, z, word):
            if node.pop(None, None):
                found.append(word)
            c = board.get(z)
            if c in node:
                board[z] = None
                for k in range(4):
                    search(node[c], z + 1j**k, word + c)
                board[z] = c
        for z in board:
            search(root, z, '')

        return found

def main():
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]] 
    words = ["oath","pea","eat","rain"]             #expect is ["oath","eat"]
    obj = Solution()
    result = obj.findWords(board, words)
    assert result == ["oath","eat"], ["hint: result is wrong"]
    print("return result is :",result)
    
if __name__ =='__main__':
    main() 