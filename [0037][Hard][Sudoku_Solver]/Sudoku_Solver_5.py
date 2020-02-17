# solution 1, back tracking.
# leetcode time     cost : 56 ms
# leetcode memory   cost : 13.1 MB 
# Time  Complexity: O(1)
# Space Complexity: O(1)
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board == None or len(board) == 0: return
        
        A = set('123456789')
        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        block = [[set() for i in range(3)] for i in range(3)]
        unfilled = []
        
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c == '.':
                    unfilled.append((i, j))
                else:
                    row[i].add(c)
                    col[j].add(c)
                    block[i//3][j//3].add(c)
                    
        def solve(board, unfilled, row, col, block):
            if len(unfilled) == 0:
                return True
            i,j = min(unfilled, key = ret_len)
            option = A-(row[i]|col[j]|block[i//3][j//3])
            if len(option) == 0:
                return False
            unfilled.remove((i,j))
            for c in option:
                board[i][j] = c
                row[i].add(c)
                col[j].add(c)
                block[i//3][j//3].add(c)
                if solve(board, unfilled, row , col, block):
                    return True
                else:
                    board[i][j] = '.'
                    row[i].remove(c)
                    col[j].remove(c)
                    block[i//3][j//3].remove(c)
            unfilled.append((i,j))
            return False
        def ret_len(args):
            i,j = args
            option = A-(row[i]|col[j]|block[i//3][j//3])
            return len(option)
                    
        solve(board, unfilled, row, col, block)