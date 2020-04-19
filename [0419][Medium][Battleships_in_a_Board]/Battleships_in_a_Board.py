# -*- coding: utf-8 -*-  
# leetcode time     cost : 80 ms
# leetcode memory   cost : 14.1 MB
# Time  Complexity: O(N)
# Space Complexity: O(1)
# solution 1, one pass loop
from typing import List
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        row = len(board)
        col = len(board[0])
        res =  0
        for i in range(row):
            for j in range(col):
                if board[i][j] == ".": continue
                if i > 0 and board[i - 1][j] == "X": continue
                if j > 0 and board[i][j - 1] == "X": continue
                res += 1
        return res
def main():
    board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
    expect = 2
    obj = Solution()
    result = obj.countBattleships(board)
    try:
        assert result == expect
        print("passed, result is follow expect:",result)
    except AssertionError as aError:
        print('failed, result is wrong', result, aError.__str__())
    
if __name__ =='__main__':
    main() 