# solution 1, back tracking.
# leetcode time     cost : 80 ms
# leetcode memory   cost : 13.1 MB 
# Time  Complexity: O(1)
# Space Complexity: O(1)
'''
Every time we find a '.', we store the possible numbers we can choose in a dict,
if the possible numbers is only one, we fill the board first and refill the board from beginning,
and last , we choose a position where the possible numbers is least to continue search
'''
class Solution:
    def solveSudoku(self, board):
        res = self.dfs(board)
        for n, row in enumerate(res):
            board[n] = ''.join(row)

    def dfs(self, board):
        stack = [board]
        while stack:
            s = stack.pop()
            result = self.fill_board(s)
            if result == 'complete':
                return s
            for r in result:
                stack.append(r)
                
    def fill_board(self, board):
        digits = set('123456789')
        choice, best = {}, []
        for j in range(9):
            for i in range(9):
                if board[j][i] == '.':
                    square = {board[j//3*3+y][i//3*3+x]
                            for y in range(3) for x in range(3)}
                    row = {board[j][x] for x in range(9)}
                    col = {board[y][i] for y in range(9)}
                    rest = digits.difference(square, row, col)
                    if len(rest) == 1:
                        board[j][i] = rest.pop()
                        return self.fill_board(board)
                    elif len(rest) == 0:
                        return ''
                    else:
                        choice[(j, i)] = rest
        if not choice:
            return 'complete'
        y, x = min(choice, key=lambda k: len(choice[k]))
        for n in choice[(y, x)]:
            b = copy.deepcopy(board)
            b[y][x] = n
            best.append(b)
        return best