# -*- coding: utf-8 -*- 
# leetcode time     cost : 40 ms
# leetcode memory   cost : 13.7 MB 
# Time  Complexity: O(1)
# Space Complexity: O(1)

# solution 1, check case by case
from typing import List
"""
To find the validity of a given board, we could first think about the cases where the board is invalid
1. Since X starts first, x_count >= o_count. So if o_count > x_count, we can return False
2. Since the players take turns, we could also return False if x_count-o_count>1

After the corner cases, this is the algorithm used:

If player O has a winning condition, also check the following:
a) If player X also has a winning condition, return False
b) If x_count != o_count , return False 
   (Since player O always plays second, it has to meet this condition always)

If player X has a winning condition, check the following:
a) If x_count != o_count + 1, return False (Since player X plays the first move, 
   if player X wins, the player X's count would be 1 more than player O)
"""
class Solution(object):
    def check_win_positions(self, board, player):
        """
        Check if the given player has a win position.
        Return True if there is a win position. Else return False.
        """
        #Check the rows
        for i in range(len(board)):
            if board[i][0] == board[i][1] == board[i][2] == player:
                return True                        

        #Check the columns
        for i in range(len(board)):
            if board[0][i] == board[1][i] == board[2][i] == player:
                return True 
										
        #Check the diagonals
        if board[0][0] == board[1][1] == board[2][2]  == player or \
               board[0][2] == board[1][1] == board[2][0] == player:
            return True
						
        return False
        
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        
        x_count, o_count = 0, 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    x_count += 1
                elif  board[i][j] == "O":
                    o_count += 1
										
        if o_count > x_count or x_count-o_count>1:
            return False
        
        if self.check_win_positions(board, 'O'):
            if self.check_win_positions(board, 'X'):
                return False
            return o_count == x_count
        
        if self.check_win_positions(board, 'X') and x_count!=o_count+1:
            return False

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