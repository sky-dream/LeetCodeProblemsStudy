# -*- coding: utf-8 -*-  
# leetcode time     cost : 424 ms
# leetcode memory   cost : 30.7 MB
class Solution:
    # def exist(self, board: List[List[str]], word: str) -> bool:
    def exist(self, board, word):
        R, C = len(board), len(board[0])

        def spread(i, j, w):
            if not w:
                return True
            original, board[i][j] = board[i][j], '-'
            spreaded = False
            for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if (0<=x<R and 0<=y<C and w[0]==board[x][y]
                        and spread(x, y, w[1:])):
                    spreaded = True
                    break
            board[i][j] = original
            return spreaded

        for i in range(R):
            for j in range(C):
                if board[i][j] == word[0] and spread(i, j, word[1:]):
                    return True
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