# -*- coding: utf-8 -*-  
# leetcode time     cost : 144 ms
# leetcode memory   cost : 14.2 MB
# Time  Complexity: O(N)
# Space Complexity: O(1)
# solution 1, one pass loop
from typing import List
class Solution(object):
    def countBattleships(self, board: List[List[str]]) -> int:
        row = len(board)
        col = len(board[0])
        count = 0
        for row_index in range(row):
            for col_index in range(col):
                f1 = False
                f2 = False
                if board[row_index][col_index] == 'X':
                    if row_index-1 >= 0:
                         if board[row_index-1][col_index] != 'X':
                                f1 = True
                    else:
                        f1 = True
                    
                    if col_index-1 >= 0:
                         if board[row_index][col_index-1] != 'X':
                                f2 = True
                    else:
                        f2 = True
                    
                    if f1 and f2:
                        count += 1
        return count
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