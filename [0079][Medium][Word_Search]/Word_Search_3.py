# -*- coding: utf-8 -*-  
# leetcode time     cost : 372 ms
# leetcode memory   cost : 30.2 MB
class Solution:
    # def exist(self, board: List[List[str]], word: str) -> bool:
    def exist(self, board, word):
        if not word:
            return True
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.exist_helper(board, word, i, j):
                    return True
        return False
                        
    def exist_helper(self, board, word, i, j):
        if board[i][j] == word[0]:
            if not word[1:]:
                return True
            board[i][j] = " " # indicate used cell
            # check all adjacent cells
            if i > 0 and self.exist_helper(board, word[1:], i-1, j):
                return True
            if i < len(board)-1 and self.exist_helper(board, word[1:], i+1, j):
                return True
            if j > 0 and self.exist_helper(board, word[1:], i, j-1):
                return True
            if j < len(board[0])-1 and self.exist_helper(board, word[1:], i, j+1):
                return True
            board[i][j] = word[0] # update the cell to its original value
            return False
        else:
            return False

def main():
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"             #expect is true
    obj = Solution()
    result = obj.exist(board, word)
    assert result == True, ["hint: result is wrong"]
    print("return result is :",result)
    
if __name__ =='__main__':
    main()  