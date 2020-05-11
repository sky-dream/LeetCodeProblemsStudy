# -*- coding: utf-8 -*- 
# leetcode time     cost : 44 ms
# leetcode memory   cost : 13.6 MB 
# Time  Complexity: O(1)
# Space Complexity: O(1)

# solution 1, check case by case
from typing import List
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        FIRST, SECOND = 'XO'
        x_count = sum(row.count(FIRST) for row in board)
        o_count = sum(row.count(SECOND) for row in board)

        def win(board, player):
            for i in range(3):
                if all(board[i][j] == player for j in range(3)):
                    return True
                if all(board[j][i] == player for j in range(3)):
                    return True

            return (player == board[1][1] == board[0][0] == board[2][2] or
                    player == board[1][1] == board[0][2] == board[2][0])

        if o_count not in {x_count-1, x_count}: return False
        if win(board, FIRST) and x_count-1 != o_count: return False
        if win(board, SECOND) and x_count != o_count: return False

        return True

def main():
    inputX,expectRes = ["XOX", "O O", "XOX"],True
    obj = Solution()
    result = obj.validTicTacToe(inputX)
    try:
        assert result == expectRes
        print("passed, result is follow expect:",result)
    except AssertionError as aError:
        print('failed, result >> ', result,"<< is wrong, ","expect is : "+ expectRes)
    
if __name__ =='__main__':
    main()    